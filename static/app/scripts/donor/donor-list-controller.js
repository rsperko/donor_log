'use strict';

angular.module('trackingApp')
  .controller('DonorListCtrl', function ($scope, metaDataService, entityResource, entityModel, alertService) {

      var setupModel = function () {
          $scope.criteria = {
            first_name: '',
            last_name: '',
            notes: '',
            donor_unset: '0'
          };
          $scope.results = [];
        },

        setupActions = function () {
          function _buildSubmit() {
            var submit = _.extend({}, $scope.criteria);

            $scope.results = [];

            return submit;
          }

          $scope.search = function () {
            var submit = _buildSubmit();

            entityResource.query(submit).$promise.then(function (result) {
              _.each(result, function (entity) {
                $scope.results.push(entityModel(entity.id, entity));
              });
            });
          };
        },

        init = function (metaData) {
          alertService.clear();

          $scope.metaData = metaData;

          setupModel(metaData);

          setupActions();
        };

      metaDataService.then(init);
    });