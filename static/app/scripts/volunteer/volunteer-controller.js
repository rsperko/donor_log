'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "metaDataService", "entityModel", "alertService",
        function ($scope, $routeParams, metaData, model, alert) {
        var self = this,
            id = $routeParams['id'],

            setupModels = function(metaData) {
                $scope.model.ensurePhone();
                $scope.model.ensureAddress();
                $scope.model.ensureVolunteerInformation();
                $scope.skills = {};
                _.each(metaData.volunteer.skill.types, function(value, key) {
                    $scope.skills[key] = $scope.model.volunteer_information[0].hasSkill(key);
                });
            },

            setupVolunteerActions = function() {
                $scope.toggleSkill = function(skill) {
                    $scope.model.volunteer_information[0].toggleSkill(skill);
                };
            },

            init = function(metaData) {
                $scope.metaData = metaData;
                $scope.model = model(id);

                self.setupEntityActions();

                setupVolunteerActions();

                if(id) {
                    $scope.model.load().then(function () {
                        setupModels(metaData);
                    });
                }
                else {
                    setupModels(metaData);
                }
            };

        new EntityControllerMixin($scope, alert).apply(self);

        metaData.then(init);
    }]);