'use strict';

angular.module('trackingApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute',
  'ui.bootstrap'
])
  .config(function ($httpProvider, $routeProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $routeProvider
      .when('/', {
        templateUrl: 'views/dashboard/main.html',
        controller: 'dashboardCtrl'
      })
      .when('/volunteer/:id?', {
        templateUrl: 'views/volunteer/main.html',
        controller: 'VolunteerCtrl'
      })
      .when('/volunteers', {
        templateUrl: 'views/volunteer/list.html',
        controller: 'VolunteerListCtrl'
      })
      .when('/donor/:id?', {
        templateUrl: 'views/donor/main.html',
        controller: 'DonorCtrl'
      })
      .when('/donors', {
        templateUrl: 'views/donor/list.html',
        controller: 'DonorListCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
