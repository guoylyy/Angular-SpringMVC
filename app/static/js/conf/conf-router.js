'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/conf/magnet', {
        templateUrl: 'views/conf/magnet_image.html',
        controller: 'MagnetConfController'
      })
      .when('/conf/main', {
        templateUrl: 'views/conf/main_image.html',
        controller: 'MainConfController'
      })
    }]);
