'use strict';

angular.module('trackingApp')
  .factory('entityModel', function ($q, $filter, entityResource, communicationResource, volunteerModel) {

      var Model = function (id, data) {
        var self = this;
        if (self instanceof Model === false) {
          self = new Model(id, data);
        }

        self.id = id;
        if (!data) {
          data = {
            addresses: [],
            email: '',
            first_name: '',
            institution_name: '',
            last_name: '',
            notes: '',
            phones: [],
            communications: [],
            volunteer_information: []
          };
        }

        self.applyData(data);

        return self;
      };

      Model.prototype.load = function () {
        var self = this,
          defer = $q.defer();

        entityResource.get({id: self.id}, function (result) {
          self.applyData(result);
          defer.resolve(self);
        });

        return defer.promise;
      };

      Model.prototype.applyData = function (data) {
        var self = this;
        _.extend(self, data);

        _.each(self.volunteer_information, function (vol_info, index) {
          self.volunteer_information[index] = volunteerModel(vol_info.id, vol_info);
        });
      };

      Model.prototype.save = function () {
        var self = this,
          defer = $q.defer(),
          action = (self.id) ? entityResource.update : entityResource.save;

        action(self).$promise.then(function (result) {
            self.applyData(result);
            defer.resolve(self);
          },
          function (error) {
            defer.reject(error);
          });

        return defer.promise;
      };

      Model.prototype.newPhone = function () {
        var self = this,
          phone = {
            primary: !self.phones.length,
            number: '',
            type: 'M'
          };
        self.phones.push(phone);
        return phone;
      };

      Model.prototype.ensurePhone = function () {
        if (!this.phones.length) {
          this.newPhone();
        }
      };

      Model.prototype.primaryPhone = function(phoneIndex) {
        _.each(this.phones, function (phone, index) {
          phone.primary = index === phoneIndex;
        });
      };

      Model.prototype.newAddress = function () {
        var self = this,
          address = {
            primary: !self.addresses.length,
            care_of: '',
            line1: '',
            line2: '',
            city: '',
            state: 'WI',
            postalCode: ''
          };
        self.addresses.push(address);
        return address;
      };

      Model.prototype.ensureAddress = function () {
        if (!this.addresses.length) {
          this.newAddress();
        }
      };

      Model.prototype.createCommunication = function () {
        var self = this,
          communication = {
            date: $filter('date')(new Date(), 'yyyy-MM-dd'),
            type: 'P',
            notes: '',
            connected: true,
            entity: self.id
          };
        return communication;
      };

      Model.prototype.saveCommunication = function (communication) {
        var self = this,
          defer = $q.defer(),
          action = (communication.id) ? communicationResource.update : communicationResource.save;

        communication.entity = self.id;

        action(communication).$promise.then(function (result) {
            if(communication.id) {
              for(var i = 0; i < self.communications.length; i++) {
                if(self.communications[i].id === communication.id) {
                  self.communications[i] = result;
                }
              }
            }
            else {
              self.communications.push(result);
            }
            defer.resolve(self);
          },
          function (error) {
            defer.reject(error);
          });

        return defer.promise;
      };

      Model.prototype.deleteCommunication = function (communication) {
        var self = this,
          defer = $q.defer();

        var success = function () {
          _.remove(self.communications, function(comm) {
            return comm.id === communication.id;
          });

          defer.resolve(self);
        };
        communicationResource.delete(communication, success);

        return defer.promise;
      };

      Model.prototype.ensureVolunteerInformation = function () {
        if (!this.volunteer_information.length) {
          this.volunteer_information.push(volunteerModel());
        }
        this.volunteer_information[0].ensureSkills();
      };

      Model.prototype.getName = function () {
        var self = this;
        if (self.institution_name) {
          return self.institution_name;
        }
        else {
          return self.first_name + ' ' + self.last_name;
        }
      };

      Model.prototype.getPrimaryPhone = function () {
        var result = _.find(this.phones, function (phone) {
          return phone.primary;
        });
        return result ? result.number : '';
      };

      return Model;
    });