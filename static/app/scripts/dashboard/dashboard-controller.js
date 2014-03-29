'use strict';

angular.module('trackingApp')
    .controller('dashboardCtrl', ["$scope", "volunteerService", function ($scope, volunteerService) {
        $scope.metadata = {};
        $scope.entities = [];

        volunteerService().then(function(volunteers) {
            $scope.entities = volunteers;
        });
    }]);
