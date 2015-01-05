'use strict';

angular.module('news')
  .factory('Movie', ['$resource', function ($resource) {
    return $resource('news/movies/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
