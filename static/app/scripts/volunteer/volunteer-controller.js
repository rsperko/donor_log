'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "volunteerModel", function ($scope, $routeParams, model) {
        var id = $routeParams['id'],

            fillFrom = function(model) {

            },

            setupActions = function() {
                $scope.save = function() {
                    $scope.model.save();
                };
            },

            init = function() {
                $scope.model = model(id);
                if(id) {
                    $scope.model.load().then(function () {
                        fillFrom($scope.model);
                    });
                }

                setupActions();
            };

        init();
    }]);