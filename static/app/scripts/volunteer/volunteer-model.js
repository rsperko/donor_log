/*global _:false */
'use strict';

angular.module('trackingApp')
  .factory('volunteerModel', ['$q', '$filter', 'volunteerResource', function ($q, $filter, resource) {

    var Model = function (id, data) {
      var self = this;
      if (self instanceof Model === false) {
        self = new Model();
      }

      self.id = id;
      if (!data) {
        data = {
          active: true,
          emergency_contact_name: '',
          emergency_contact_number: '',
          skills: []
        };
      }
      self.applyData(data);

      return self;
    };

    Model.prototype.load = function () {
      var self = this,
        defer = $q.defer();

      resource.get({id: self.id}, function (result) {
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
        resource.update(self, success);
      }
      else {
        resource.save(self, success);
      }

      return defer.promise;
    };

    Model.prototype.ensureSkills = function () {
      if (!this.skills) {
        this.skills = [];
      }
    };

    Model.prototype.hasSkill = function (skillCode) {
      var self = this,
        ret = _.findIndex(self.skills, function (skill) {
          return skill.type === skillCode;
        });
      return ret !== -1;
    };

    Model.prototype.toggleSkill = function (skillCode) {
      var self = this;
      var index = _.findIndex(self.skills, function (skill) {
        return skill.type === skillCode;
      });

      if (index >= 0) {
        self.skills.splice(index, 1);
      }
      else {
        self.skills.push({ type: skillCode });
      }
    };


    return Model;
  }]);