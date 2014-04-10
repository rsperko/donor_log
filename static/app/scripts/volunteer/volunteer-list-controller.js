'use strict';

angular.module('trackingApp')
  .controller('VolunteerListCtrl', function ($scope, metaDataService, entityResource, entityModel, alertService) {

      var setupModel = function (metaData) {
          $scope.skills = {};
          $scope.criteria = {
            first_name: '',
            last_name: '',
            skills: '',
            notes: '',
            volunteer_unset: '0'
          };
          $scope.results = [];
          _.each(metaData.volunteer.skill.types, function (value, key) {
            $scope.skills[key] = false;
          });
        },

        setupActions = function () {
          var _applyApplicableVolunteerCriteria = function(criteria) {
            var selectedSkills = [];
              if(criteria.is_volunteer === 'True') {
                _.each($scope.skills, function (value, key) {
                  if (value) {
                    selectedSkills.push(key);
                  }
                });
                criteria.skills = selectedSkills.join();
              }
              return criteria;
            },

            _buildSubmitCriteria = function() {
              var criteria = _.extend({}, $scope.criteria);

              $scope.results = [];

              criteria = _applyApplicableVolunteerCriteria(criteria);

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