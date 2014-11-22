'use strict';

angular.module('news')
  .controller('UserController', ['$scope', '$modal', 'resolvedUser', 'User',
    function ($scope, $modal, resolvedUser, User) {

      $scope.users = resolvedUser;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.user = User.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        User.delete({id: id},
          function () {
            $scope.users = User.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          User.update({id: id}, $scope.user,
            function () {
              $scope.users = User.query();
              $scope.clear();
            });
        } else {
          User.save($scope.user,
            function () {
              $scope.users = User.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.user = {
          
          "account": "",
          
          "password": "",
          
          "name": "",
          
          "role": "",
          
          "email": "",
          
          "registered_time": "",
          
          "is_active": "",
          
          "phone_number": "",
          
          "description": "",
          
          "lastlogin_time": "",
          
          "myattr": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var userSave = $modal.open({
          templateUrl: 'user-save.html',
          controller: UserSaveController,
          resolve: {
            user: function () {
              return $scope.user;
            }
          }
        });

        userSave.result.then(function (entity) {
          $scope.user = entity;
          $scope.save(id);
        });
      };
    }]);

var UserSaveController =
  function ($scope, $modalInstance, user) {
    $scope.user = user;

    
    $scope.registered_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };
    $scope.lastlogin_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };

    $scope.ok = function () {
      $modalInstance.close($scope.user);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
