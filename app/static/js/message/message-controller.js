'use strict';

angular.module('news')
  .controller('MessageController', ['$scope', '$modal', 'resolvedMessage', 'Message', '$filter',
    function($scope, $modal, resolvedMessage, Message, $filter) {

      $scope.messages = resolvedMessage;

      $scope.create = function() {
        $scope.clear();
        $scope.open(null, true);
      };

      $scope.update = function(id) {
        $scope.message = Message.get({
          id: id
        });
        $scope.open(id, false);
      };

      $scope.delete = function(id) {
        Message.delete({
            id: id
          },
          function() {
            $scope.messages = Message.query();
          });
      };

      $scope.save = function(id) {
        if (id) {
          Message.update({
              id: id
            }, $scope.message,
            function() {
              $scope.messages = Message.query();
              $scope.clear();
            });
        } else {
          Message.save($scope.message,
            function() {
              $scope.messages = Message.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function() {
        $scope.message = {

          "content": "",

          "created_time": "",

          "publisher": "",

          "is_active": true,

          "id": ""
        };
      };

      $scope.open = function(id, is_create) {
        var template = 'message-save.html';
        if(is_create){
          template = 'message-create.html';
        }
        var messageSave = $modal.open({
          templateUrl: template,
          controller: MessageSaveController,
          resolve: {
            message: function() {
              return $scope.message;
            }
          }
        });

        messageSave.result.then(function(entity) {
          $scope.message = entity;
          // $scope.message.started_time = $filter('date')($scope.message.started_time,
          //    'yyyy-MM-dd HH:mm:ss');
          $scope.save(id);
        });
      };
    }
  ]);

var MessageSaveController =
  function($scope, $modalInstance, message, $filter) {
    $scope.message = message;
    $scope.$watch(function() {
        return $scope.message.created_time;
      },
      function(newValue, oldValue) {
        if(newValue != undefined && newValue.indexOf('T')> -1){
          $scope.message.created_time = $filter('date')(newValue,
          'yyyy-MM-dd HH:mm:ss');
        };
      });

    $scope.created_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
    };
    $scope.onTimeSet = function(newDate, oldDate) {
      $scope.message.created_time = $filter('date')(newDate,
        'yyyy-MM-dd HH:mm:ss');
    };
    $scope.ok = function() {
      $modalInstance.close($scope.message);
    };

    $scope.cancel = function() {
      $modalInstance.dismiss('cancel');
    };
  };