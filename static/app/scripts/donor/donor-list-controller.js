'use strict';

angular.module('trackingApp')
  .controller('DonorListCtrl', function ($scope, metaDataService, entityResource, entityModel, alertService) {

    var setupModel = function () {
        $scope.categories = {};
        $scope.types = {};
        $scope.criteria = {
          institution_name: '',
          first_name: '',
          last_name: '',
          notes: '',
          donor_unset: '0',
        };
        $scope.results = [];
      },

      setupActions = function () {
        var _applyApplicableDonorCriteria = function (criteria) {
            var selectedCategories = [];
            _.each($scope.categories, function (value, key) {
              if (value) {
                selectedCategories.push(key);
              }
            });
            criteria.donor_categories = selectedCategories.join();

            var selectedTypes = [];
            _.each($scope.types, function (value, key) {
              if (value) {
                selectedTypes.push(key);
              }
            });
            criteria.donor_types = selectedTypes.join();

            return criteria;
          },

          _buildSubmitCriteria = function () {
            var criteria = _.extend({}, $scope.criteria);

            $scope.results = [];

            criteria = _applyApplicableDonorCriteria(criteria);

            return criteria;
          };

        $scope.search = function () {
          var submit = _buildSubmitCriteria();

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