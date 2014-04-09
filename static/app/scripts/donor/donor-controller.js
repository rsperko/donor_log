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

          $scope.saveDonation = function () {
            alertService.clear();
            $scope.model.donor_information[0].donations.push($scope.currentDonation);
            $scope.currentDonation = null;
          };

          $scope.cancelDonation = function () {
            $scope.currentDonation = null;
          };

          $scope.deleteDonation = function (donationIndex) {
            alertService.clear();
            $scope.model.donor_information[0].donations.splice(donationIndex, 1);
          };

          $scope.editDonation = function (donationIndex) {
            $scope.currentDonation = _.extend({}, $scope.model.donor_information[0].donations[donationIndex]);
          };

          $scope.donationDateOpen = function($event) {
            $event.preventDefault();
            $event.stopPropagation();

            $scope.donationDateOpened = true;
          };
          
          $scope.createDonation = function() {
            $scope.currentDonation = $scope.model.donor_information[0].createDonation();
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