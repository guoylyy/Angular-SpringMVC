'use strict';

angular.module('news')
  .controller('InformController', ['$scope', '$modal', 'resolvedInform', 'Inform',
    function ($scope, $modal, resolvedInform, Inform) {

      $scope.informs = resolvedInform;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.inform = Inform.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Inform.delete({id: id},
          function () {
            $scope.informs = Inform.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Inform.update({id: id}, $scope.inform,
            function () {
              $scope.informs = Inform.query();
              $scope.clear();
            });
        } else {
          Inform.save($scope.inform,
            function () {
              $scope.informs = Inform.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.inform = {
          
          "title": "",
          
          "create_time": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var informSave = $modal.open({
          templateUrl: 'inform-save.html',
          controller: InformSaveController,
          resolve: {
            inform: function () {
              return $scope.inform;
            }
          }
        });

        informSave.result.then(function (entity) {
          $scope.inform = entity;
          $scope.save(id);
        });
      };
    }]);

var InformSaveController =
  function ($scope, $modalInstance, inform) {
    $scope.inform = inform;

    
    $scope.create_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };

    $scope.ok = function () {
      $modalInstance.close($scope.inform);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
