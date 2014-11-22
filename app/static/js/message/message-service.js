'use strict';

angular.module('news')
  .factory('Message', ['$resource', function ($resource) {
    return $resource('news/messages/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
