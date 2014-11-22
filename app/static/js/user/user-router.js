'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/users', {
        templateUrl: 'views/user/users.html',
        controller: 'UserController',
        resolve:{
          resolvedUser: ['User', function (User) {
            return User.query();
          }]
        }
      })
    }]);
