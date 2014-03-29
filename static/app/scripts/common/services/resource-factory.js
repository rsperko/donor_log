'use strict';

angular.module('trackingApp')
    .factory("resourceFactory", ["$resource", function($resource) {
        var factory = function(url, params, custom) {
            return $resource(url, params || {}, _.extend({}, custom || {}, {"update": {"method":"PUT"}}));
        };

        return factory;
    }]);