'use strict';

angular.module('news')
  .factory('News', ['$resource', function ($resource) {
    return $resource('news/news/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
