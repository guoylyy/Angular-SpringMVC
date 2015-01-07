// Declare app level module which depends on filters, and services
angular.module('news', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date',
    'ui.bootstrap.datetimepicker', 'ngCkeditor', 'angularFileUpload', 'ngStorage',
    'inform','datatables'
  ])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginController'
      })
      .otherwise({
        redirectTo: '/'
      });
  }]);