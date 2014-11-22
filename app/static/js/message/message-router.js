'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/messages', {
        templateUrl: 'views/message/messages.html',
        controller: 'MessageController',
        resolve:{
          resolvedMessage: ['Message', function (Message) {
            return Message.query();
          }]
        }
      })
    }]);
