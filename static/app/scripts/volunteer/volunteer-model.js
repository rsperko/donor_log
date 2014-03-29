'use strict';

angular.module('trackingApp')
    .factory('volunteerModel', ["$q", "$filter", "volunteerResource", function($q, $filter, resource) {

        var Model = function(id, data) {
            var self = this;
            if (self instanceof Model === false) {
                self = new Model();
            }

            self.id = id;
            if(! data) {
                data = {
                    active: true,
                    emergency_contact_name: '',
                    emergency_contact_number: '',
                    skills: []
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

        Model.prototype.ensureSkills = function() {
            if(! this.skills) {
                this.skills = [];
            }
        };


        return Model;
    }]);