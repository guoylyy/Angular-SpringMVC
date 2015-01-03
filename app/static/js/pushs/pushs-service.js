'use strict';

angular.module('news')
  .factory('Pushs', ['$resource', function ($resource) {
    return $resource('news/pushs/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
