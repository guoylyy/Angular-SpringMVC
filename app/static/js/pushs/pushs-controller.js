'use strict';

angular.module('news')
  .controller('PushsController', ['$scope', '$modal', 'resolvedPushs', 'Pushs',
    function ($scope, $modal, resolvedPushs, Pushs) {

      $scope.push_array = resolvedPushs;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.pushs = Pushs.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Pushs.delete({id: id},
          function () {
            $scope.push_array = Pushs.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Pushs.update({id: id}, $scope.pushs,
            function () {
              $scope.push_array = Pushs.query();
              $scope.clear();
            });
        } else {
          Pushs.save($scope.pushs,
            function () {
              $scope.push_array = Pushs.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.pushs = {
          
          "content": "",
          
          "created_time": "",
          
          "success": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var pushsSave = $modal.open({
          templateUrl: 'pushs-save.html',
          controller: PushsSaveController,
          resolve: {
            pushs: function () {
              return $scope.pushs;
            }
          }
        });

        pushsSave.result.then(function (entity) {
          $scope.pushs = entity;
          $scope.save(id);
        });
      };
    }]);

var PushsSaveController =
  function ($scope, $modalInstance, pushs) {
    $scope.pushs = pushs;

    
    $scope.created_timeDateOptions = {
      dateFormat: 'yy-mm-dd',

    };

    $scope.ok = function () {
      $modalInstance.close($scope.pushs);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
