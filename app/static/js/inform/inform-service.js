'use strict';

angular.module('news')
  .factory('Inform', ['$resource', function ($resource) {
    return $resource('news/informs/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
