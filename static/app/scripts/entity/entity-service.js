'use strict';

angular.module('trackingApp')
    .factory('entityResource', ["resourceFactory", function(resourceFactory) {
        var service = resourceFactory("/api/entities/:entity/:id/:action",
            {
                id:"@id",
                entity:"@entity"
            }, {
                'addCommunication': {method: 'POST', params: { action: 'communications' }},
                'deleteCommunication': {method: 'DELETE', params: { action: 'communications' }}
            });
        return service;
    }])
    .factory('entityService', ["entityModel", "$http", "$q", function(entityModel, $http, $q) {
        var load = function() {
            var defer = $q.defer();

            $http.get('/api/entities/').then(function(result) {
                var ret = [];

                _.each(result.data, function(data) {
                    var items = entityModel(data.id, data);
                    ret.push(items);
                });

                defer.resolve(ret);
            });

            return defer.promise;
        };
        return load;
    }]);