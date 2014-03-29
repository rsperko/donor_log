'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "volunteerModel", function ($scope, $routeParams, model) {
        $scope.model = model($routeParams['entityId']);
        $scope.model.load().then(function(){
            console.log($scope.model);
        });
    }]);