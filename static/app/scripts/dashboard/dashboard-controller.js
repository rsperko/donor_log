'use strict';

angular.module('staticApp')
    .controller('DashboardCtrl', function ($scope, $http) {
        $scope.metadata = {};
        $scope.entities = [];

        $http.get('/entity/').then(function(result) {
            angular.forEach(result.data, function(entity) {
                $scope.entities.push(entity);
            })
        });
    });
