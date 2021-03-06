'use strict';

angular.module('trackingApp')
  .factory('donorModel', function ($q, $filter, donorResource) {

    var Model = function (id, data) {
      var self = this;
      if (self instanceof Model === false) {
        self = new Model();
      }

      self.id = id;
      if (!data) {
        data = {
          category: 'I',
          type: 'D',
          donations: []
        };
      }
      self.applyData(data);

      return self;
    };

    Model.prototype.load = function () {
      var self = this,
        defer = $q.defer();

      donorResource.get({id: self.id}, function (result) {
        self.applyData(result);
        defer.resolve(self);
      });

      return defer.promise;
    };

    Model.prototype.applyData = function (data) {
      var self = this;
      _.extend(self, data);
    };

    Model.prototype.save = function () {
      var self = this,
        defer = $q.defer();

      var success = function (result) {
        self.applyData(result);
        defer.resolve(self);
      };
      if (self.id) {
        donorResource.update(self, success);
      }
      else {
        donorResource.save(self, success);
      }

      return defer.promise;
    };

    Model.prototype.createDonation = function() {
      return {
        date: $filter('date')(new Date(), 'yyyy-MM-dd'),
        monetary_amount: null,
        type: 'F',
        notes: null
      };
    };

    Model.prototype.isIndividual = function() {
      return this.category === 'I';
    };

    Model.prototype.getTotalDonated = function() {
      var self = this,
        result = 0.00;

      _.each(self.donations, function(donation) {
        result += donation.monetary_amount;
      });

      return result;
    };

    return Model;
  });