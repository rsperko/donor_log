'use strict';

angular.module('trackingApp')
  .factory('entityResource', ['resourceFactory', function (resourceFactory) {
    var service = resourceFactory('/api/entities/:entity/:id/:action',
      {
        id: '@id',
        entity: '@entity'
      }, {
        'addCommunication': {method: 'POST', params: { action: 'communications' }},
        'deleteCommunication': {method: 'DELETE', params: { action: 'communications' }}
      });
    return service;
  }]);