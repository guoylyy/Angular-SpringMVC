'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/conferences', {
        templateUrl: 'views/conference/conferences.html',
        controller: 'ConferenceController',
        resolve:{
          resolvedConference: ['Conference', function (Conference) {
            return Conference.query();
          }]
        }
      })
    }]);
