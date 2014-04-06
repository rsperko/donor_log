'use strict';

angular.module('trackingApp')
  .controller('VolunteerCtrl', function ($scope, $routeParams, $q, $controller, metaDataService, entityModel, alertService) {
      var entityCtrl = $controller('EntityCtrl', {$scope: $scope, alertService: alertService, $q: $q}),
        id = $routeParams.id,

        setupModels = function () {
          $scope.model.ensurePhone();
          $scope.model.ensureAddress();
          $scope.model.ensureVolunteerInformation();
          $scope.skills = {};
          _.each($scope.metaData.volunteer.skill.types, function (value, key) {
            $scope.skills[key] = $scope.model.volunteer_information[0].hasSkill(key);
          });
        },

        setupVolunteerActions = function () {
          $scope.toggleSkill = function (skill) {
            $scope.model.volunteer_information[0].toggleSkill(skill);
          };

          $scope.saveAndNew = function () {
            alertService.clear();
            $scope.save().then(function () {
              $scope.model = entityModel();
              setupModels();
            });
          };
        },

        init = function (metaData) {
          alertService.clear();

          $scope.metaData = metaData;
          $scope.model = entityModel(id);

          entityCtrl.setupEntityActions();

          setupVolunteerActions();

          if (id) {
            $scope.model.load().then(function () {
              setupModels();
            });
          }
          else {
            setupModels();
          }
        };

      metaDataService.then(init);
    });