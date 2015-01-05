'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/movies', {
        templateUrl: 'views/movie/movies.html',
        controller: 'MovieController',
        resolve:{
          resolvedMovie: ['Movie', function (Movie) {
            return Movie.query();
          }]
        }
      })
    }]);
