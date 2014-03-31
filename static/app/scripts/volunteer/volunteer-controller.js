'use strict';

angular.module('trackingApp')
    .controller('volunteerCtrl', ["$scope", "$routeParams", "$q", "metaDataService", "entityModel", "alertService",
        function ($scope, $routeParams, $q, metaData, model, alert) {
        var self = this,
            id = $routeParams['id'],

            setupModels = function() {
                $scope.model.ensurePhone();
                $scope.model.ensureAddress();
                $scope.model.ensureVolunteerInformation();
                $scope.skills = {};
                _.each($scope.metaData.volunteer.skill.types, function(value, key) {
                    $scope.skills[key] = $scope.model.volunteer_information[0].hasSkill(key);
                });
            },

            setupVolunteerActions = function() {
                $scope.toggleSkill = function(skill) {
                    $scope.model.volunteer_information[0].toggleSkill(skill);
                };

                $scope.saveAndNew = function() {
                    $scope.save().then(function(result) {
                        $scope.model = model();
                        setupModels();
                    });
                };
            },

            init = function(metaData) {
                $scope.metaData = metaData;
                $scope.model = model(id);

                self.setupEntityActions();

                setupVolunteerActions();

                if(id) {
                    $scope.model.load().then(function () {
                        setupModels();
                    });
                }
                else {
                    setupModels();
                }
            };

        new EntityControllerMixin($scope, alert, $q).apply(self);

        metaData.then(init);
    }]);