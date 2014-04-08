'use strict';

angular.module('trackingApp')
  .factory('donorResource', function (resourceFactory) {
    var service = resourceFactory('/api/donors/:id/:action',
      {
        id: '@id'
      }, {
      });
    return service;
  })
  .factory('donorService', function (donorModel, $http, $q) {
    var load = function () {
      var defer = $q.defer();

      $http.get('/api/donors/').then(function (result) {
        var ret = [];

        _.each(result.data, function (data) {
          var items = donorModel(data.id, data);
          ret.push(items);
        });

        defer.resolve(ret);
      });

      return defer.promise;
    };
    return load;
  });