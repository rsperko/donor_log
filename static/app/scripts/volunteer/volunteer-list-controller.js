/*global _:false */
'use strict';

angular.module('trackingApp')
  .controller('volunteerListCtrl', ['$scope', 'metaDataService', 'entityResource', 'entityModel', 'alertService',
    function ($scope, metaData, resource, entityModel, alert) {

      var setupModel = function (metaData) {
        $scope.skills = {};
        $scope.criteria = {
          first_name: '',
          last_name: '',
          active: true,
          skills: ''
        };
        $scope.results = [];
        _.each(metaData.volunteer.skill.types, function (value, key) {
          $scope.skills[key] = false;
        });
      },

        setupActions = function () {
          $scope.search = function () {
            var submit = _.extend({}, $scope.criteria);
            submit.active = (submit.active) ? 'True' : 'False';

            $scope.results = [];

            var selectedSkills = [];
            _.each($scope.skills, function (value, key) {
              if (value) {
                selectedSkills.push(key);
              }
            });
            submit.skills = selectedSkills.join();
            resource.query(submit).$promise.then(function (result) {
              _.each(result, function (entity) {
                $scope.results.push(entityModel(entity.id, entity));
              });
            });
          };
        },

        init = function (metaData) {
          alert.clear();

          $scope.metaData = metaData;

          setupModel(metaData);

          setupActions();
        };

      metaData.then(init);
    }]);