'use strict';

angular.module('news')
  .factory('Conference', ['$resource', function ($resource) {
    return $resource('news/conferences/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
