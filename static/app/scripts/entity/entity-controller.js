'use strict';

angular.module('trackingApp')
  .controller('EntityCtrl', function ($scope, alertService, $q) {
    var self = this;

    self.setupEntityActions = function () {
      $scope.save = function () {
        alertService.clear();
        var defer = $q.defer();
        $scope.model.save().then(function (result) {
            alertService.add('success', 'Saved successfully');
            defer.resolve(result);
          },
          function (error) {
            alertService.add('danger', 'Failed to save ' + angular.toJson(error.data));
            defer.reject(error);
          });
        return defer.promise;
      };

      $scope.addPhone = function () {
        $scope.model.newPhone();
      };

      $scope.deletePhone = function (phoneIndex) {
        var deleted = $scope.model.phones.splice(phoneIndex, 1);
        if (deleted.length && deleted[0].primary && $scope.model.phones.length) {
          $scope.model.phones[0].primary = true;
        }
      };

      $scope.primaryPhone = function (phoneIndex) {
        $scope.model.primaryPhone(phoneIndex);
      };

      $scope.createCommunication = function () {
        $scope.currentCommunication = $scope.model.createCommunication();
      };

      $scope.saveCommunication = function () {
        alertService.clear();
        $scope.model.saveCommunication($scope.currentCommunication);
        $scope.currentCommunication = null;
      };

      $scope.cancelCommunication = function () {
        $scope.currentCommunication = null;
      };

      $scope.deleteCommunication = function (communicationIndex) {
        alertService.clear();
        $scope.model.deleteCommunication($scope.model.communications[communicationIndex]);
      };

      $scope.editCommunication = function (communicationIndex) {
        $scope.currentCommunication = _.extend({}, $scope.model.communications[communicationIndex]);
      };
    };
  });
