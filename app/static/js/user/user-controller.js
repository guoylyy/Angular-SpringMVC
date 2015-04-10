'use strict';

angular.module('news')
  .controller('UserController', ['$scope', '$modal', 'resolvedUser', 'User', 'DTOptionsBuilder', 'DTColumnDefBuilder',
    function ($scope, $modal, resolvedUser, User, DTOptionsBuilder, DTColumnDefBuilder) {

      $scope.users = resolvedUser;
      $scope.dtOptions = DTOptionsBuilder.newOptions()
          .withOption('order',[0,'desc']);

      $scope.dtColumnDefs = [
          DTColumnDefBuilder.newColumnDef(0),
          DTColumnDefBuilder.newColumnDef(1),
          DTColumnDefBuilder.newColumnDef(2),
          DTColumnDefBuilder.newColumnDef(3),
          DTColumnDefBuilder.newColumnDef(4).notSortable(),
          DTColumnDefBuilder.newColumnDef(5).notSortable()
      ];
      $scope.create = function () {
        $scope.clear();
        $scope.open('', true);
      };

      $scope.update = function (id) {
        $scope.user = User.get({id: id});
        $scope.open(id, false);
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
            },function(e){
              alert('该用户名已存在，更新用户失败！');
            });
        } else {
          User.save($scope.user,
            function () {
              $scope.users = User.query();
              $scope.clear();
            },function(e){
              alert('该用户名已存在，添加用户失败！');
            });
        }
      };

      $scope.clear = function () {
        $scope.user = {
          
          "account": "",
          
          "password": "",
          
          "name": "",
          
          "role": "",

          "is_vip" : false,

          "nickname" : "",
          
          "email": "",

          "title": "",
          
          "registered_time": "",
          
          "is_active": "",
          
          "phone_number": "",
          
          "description": "",
          
          "lastlogin_time": "",
          
          "myattr": "",
          
          "id": ""
        };
      };

      $scope.open = function (id, is_create) {
        var template = 'user-save.html';
        if(is_create){
          template = 'user-create.html';
        }

        var userSave = $modal.open({
          templateUrl: template,
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
