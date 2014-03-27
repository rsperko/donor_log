'use strict';

angular.module('staticApp')
    .controller('MainCtrl', function ($scope, $http) {
        $scope.metadata = {};
        $scope.entities = [];

        $http.get('/entity/').then(function(result) {
            angular.forEach(result.data, function(entity) {
                $scope.entities.push(entity);
            })
        });
    });