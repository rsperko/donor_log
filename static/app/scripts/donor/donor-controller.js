'use strict';

angular.module('trackingApp')
  .controller('DonorCtrl', function ($scope, $routeParams, $q, $controller, metaDataService, entityModel, alertService) {
      var entityCtrl = $controller('EntityCtrl', {$scope: $scope, alertService: alertService, $q: $q}),
        id = $routeParams.id,

        setupModels = function () {
          $scope.model.ensurePhone();
          $scope.model.ensureAddress();
          $scope.model.ensureDonorInformation();
        },

        setupDonorActions = function () {
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

          setupDonorActions();

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