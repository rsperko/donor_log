'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "volunteerModel", function ($scope, $routeParams, model) {
        var id = $routeParams['id'],

            fillFromModel = function() {
                if(! $scope.model.phones.length) {
                    $scope.model.newPhone();
                }
                if(! $scope.model.addresses.length) {
                    $scope.model.newAddress();
                }
            },

            setupActions = function() {
                $scope.save = function() {
                    $scope.model.save();
                };

                $scope.addPhone = function() {
                    $scope.model.newPhone();
                };

                $scope.deletePhone = function(phoneIndex) {
                    var deleted = $scope.model.phones.splice(phoneIndex, 1);
                    if(deleted.primary && $scope.model.phones.length) {
                        $scope.model.phones[0].primary = true;
                    }
                };

                $scope.primaryPhone = function(phoneIndex) {
                    _.each($scope.model.phones, function(phone, index) {
                        phone.primary = index === phoneIndex;
                    });
                };
            },

            init = function() {
                $scope.model = model(id);
                if(id) {
                    $scope.model.load().then(function () {
                        fillFromModel();
                    });
                }
                else {
                    fillFromModel();
                }

                setupActions();
            };

        init();
    }]);