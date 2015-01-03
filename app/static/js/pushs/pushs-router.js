'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/pushs', {
        templateUrl: 'views/pushs/pushs.html',
        controller: 'PushsController',
        resolve:{
          resolvedPushs: ['Pushs', function (Pushs) {
            return Pushs.query();
          }]
        }
      })
    }]);
