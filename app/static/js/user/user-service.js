'use strict';

angular.module('news')
  .factory('User', ['$resource', function ($resource) {
    return $resource('news/users/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
