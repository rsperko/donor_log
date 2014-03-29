'use strict';

angular.module('trackingApp')
    .factory('entityModel', ["$q", "$filter", "entityResource", "volunteerModel", function($q, $filter, resource, volunteerModel) {

        var Model = function(id, data) {
            var self = this;
            if (self instanceof Model === false) {
                self = new Model();
            }

            self.id = id;
            if(! data) {
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
            _.extend(self, data);

            return self;
        };

        Model.prototype.load = function() {
            var self = this,
                defer = $q.defer();

            resource.get({id: self.id}, function(result) {
                _.extend(self, result);
                defer.resolve(self);
            });

            return defer.promise;
        };

        Model.prototype.save = function() {
            var self = this,
                defer = $q.defer();

            var success = function (result) {
                _.extend(self, result);
                defer.resolve(self);
            };
            if(self.id) {
                resource.update(self, success);
            }
            else {
                resource.save(self, success);
            }

            return defer.promise;
        };

        Model.prototype.newPhone = function() {
            var self = this,
                phone = {
                primary: ! self.phones.length,
                number: '',
                type: ''
            };
            self.phones.push(phone);
            return phone;
        };

        Model.prototype.ensurePhone = function() {
            if(! this.phones.length) {
                this.newPhone();
            }
        };

        Model.prototype.newAddress = function() {
            var self = this,
                address = {
                    primary: ! self.addresses.length,
                    care_of: '',
                    line1: '',
                    line2: '',
                    city: '',
                    state: '',
                    postalCode: ''
                };
            self.addresses.push(address);
            return address;
        };

        Model.prototype.ensureAddress = function() {
            if(! this.addresses.length) {
                this.newAddress();
            }
        };

        Model.prototype.createCommunication = function() {
            var self = this,
                communication = {
                    date: $filter('date')(new Date(), 'yyyy-MM-dd'),
                    type: '',
                    notes: '',
                    connected: true,
                    entity: self.id
                };
            return communication;
        };

        Model.prototype.addCommunication = function(communication) {
            var self = this,
                defer = $q.defer();

            var success = function (result) {
                _.extend(self, result);
                defer.resolve(self);
            };
            resource.addCommunication(communication, success);

            return defer.promise;
        };

        Model.prototype.deleteCommunication = function(communication) {
            var self = this,
                defer = $q.defer();

            var success = function (result) {
                _.extend(self, result);
                defer.resolve(self);
            };
            resource.deleteCommunication({id: self.id, comm_id: communication.id}, success);

            return defer.promise;
        };

        Model.prototype.ensureVolunteerInformation = function() {
            if(! this.volunteer_information.length) {
                this.volunteer_information.push(volunteerModel());
            }
            this.volunteer_information[0].ensureSkills();
        };

        return Model;
    }]);