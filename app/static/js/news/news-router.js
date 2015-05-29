'use strict';

angular.module('news')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/news', {
        templateUrl: 'views/news/news.html',
        controller: 'NewsController',
        resolve:{
          resolvedNews: ['SimpleNews', function (SimpleNews) {
            return SimpleNews.query();
          }]
        }
      })
    }]);
