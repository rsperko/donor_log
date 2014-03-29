'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "entityModel", function ($scope, $routeParams, model) {
        var self = this,
            id = $routeParams['id'],

            fillFromModel = function() {
                $scope.model.ensurePhone();
                $scope.model.ensureAddress();
                $scope.model.ensureVolunteerInformation();
            },

            init = function() {
                $scope.model = model(id);

                self.setupEntityActions();

                if(id) {
                    $scope.model.load().then(function () {
                        fillFromModel();
                    });
                }
                else {
                    fillFromModel();
                }
            };

        _.extend(self, new EntityControllerMixin($scope));

        init();
    }]);