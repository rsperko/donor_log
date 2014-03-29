'use strict';

angular.module('trackingApp')
    .factory('volunteerModel', ["volunteerResource", "$q", function(resource, $q) {

        var Model = function(id, data) {
            var self = this;
            if (self instanceof Model === false) {
                self = new Model();
            }

            self.id = id;
            self.data = data;

            return self;
        };

        Model.prototype.load = function() {
            var self = this,
                defer = $q.defer();

            resource.get({id: self.id}, function(result) {
                self.data = result;
                defer.resolve(self);
            });

            return defer.promise;
        };

        Model.prototype.save = function() {
            var self = this,
                defer = $q.defer();

            resource.update(self.data, function(result) {
                self.data = result;
                defer.resolve(self);
            });

            return defer.promise;
        };

        return Model;
    }]);