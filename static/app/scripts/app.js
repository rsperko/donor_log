'use strict';

angular.module('trackingApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/dashboard/main.html',
        controller: 'dashboardCtrl'
      })
      .when('/volunteer/:id?', {
        templateUrl: 'views/volunteer/main.html',
        controller: 'volunteerCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
