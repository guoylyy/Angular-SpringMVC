'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/informs', {
        templateUrl: 'views/inform/informs.html',
        controller: 'InformController',
        resolve:{
          resolvedInform: ['Inform', function (Inform) {
            return Inform.query();
          }]
        }
      })
    }]);
