'use strict';

angular.module('news')
  .controller('MessageController', ['$scope', '$modal', 'resolvedMessage', 'Message',
    function($scope, $modal, resolvedMessage, Message) {

      $scope.messages = resolvedMessage;

      $scope.create = function() {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function(id) {
        $scope.message = Message.get({
          id: id
        });
        $scope.open(id);
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

      $scope.open = function(id) {
        var messageSave = $modal.open({
          templateUrl: 'message-save.html',
          controller: MessageSaveController,
          resolve: {
            message: function() {
              return $scope.message;
            }
          }
        });

        messageSave.result.then(function(entity) {
          $scope.message = entity;
          $scope.save(id);
        });
      };
    }
  ]);

var MessageSaveController =
  function($scope, $modalInstance, message, $filter) {
    $scope.message = message;
    $scope.created_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
    };
    $scope.$watch(function(scope) {
        return scope.message.created_time
      },
      function(newValue, oldValue) {
        if (newValue != undefined) {
          var n_date = $filter('date')(newValue,
            'yyyy-MM-dd HH:mm:ss');
          $scope.message.created_time = n_date;
        }
      });
    $scope.ok = function() {
      $modalInstance.close($scope.message);
    };

    $scope.cancel = function() {
      $modalInstance.dismiss('cancel');
    };
  };