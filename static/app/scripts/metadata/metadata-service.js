'use strict';

angular.module('trackingApp')
  .factory('metaDataService', ['$http', '$q', function ($http, $q) {
//        var load = function() {
    var defer = $q.defer();

    $http.get('/api/meta_data/').then(function (result) {
      defer.resolve(result.data);
    });

    return defer.promise;
//        };
//        return load();
  }]);