'use strict';

angular.module('trackingApp')
    .factory('volunteerModel', ["volunteerResource", "$q", function(resource, $q) {

        var Model = function(entityId, data) {
            var self = this;
            if (self instanceof Model === false) {
                self = new Model();
            }

            self.entityId = entityId;
            self.data = data;

            return self;
        };

        Model.prototype.load = function() {
            var self = this,
                defer = $q.defer();

            resource.get({entityId: self.entityId}, function(result) {
                self.data = result;
                defer.resolve(self);
            });

            return defer.promise;
        };

        return Model;
    }]);