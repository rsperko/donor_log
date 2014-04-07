'use strict';

angular.module('trackingApp')
  .factory('entityResource', function (resourceFactory) {
    var service = resourceFactory('/api/entities/:entity/:action/:id',
      {
        id: '@id',
        entity: '@entity'
      }, {
        'addCommunication': {method: 'POST', params: { action: 'communications' }},
        'updateCommunication': {method: 'PUT', params: { action: 'communications' }},
        'deleteCommunication': {method: 'DELETE', params: { action: 'communications' }}
      });
    return service;
  })
  .factory('communicationResource', function (resourceFactory) {
    var service = resourceFactory('/api/communications/:id',
      {
        id: '@id'
      });
    return service;
  });