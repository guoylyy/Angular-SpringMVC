'use strict';

angular.module('news')
  .controller('ConferenceController', ['$scope', '$modal', 'resolvedConference', 'Conference',
    function ($scope, $modal, resolvedConference, Conference) {

      $scope.conferences = resolvedConference;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.conference = Conference.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Conference.delete({id: id},
          function () {
            $scope.conferences = Conference.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Conference.update({id: id}, $scope.conference,
            function () {
              $scope.conferences = Conference.query();
              $scope.clear();
            });
        } else {
          Conference.save($scope.conference,
            function () {
              $scope.conferences = Conference.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.conference = {
          
          "intro_content": "",
          
          "logistics_content": "",
          
          "title": "",
          
          "created_time": "",
          
          "updated_time": "",
          
          "view_count": "",
          
          "is_draft": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var conferenceSave = $modal.open({
          templateUrl: 'conference-save.html',
          controller: ConferenceSaveController,
          resolve: {
            conference: function () {
              return $scope.conference;
            }
          }
        });

        conferenceSave.result.then(function (entity) {
          $scope.conference = entity;
          $scope.save(id);
        });
      };
    }]);

var ConferenceSaveController =
  function ($scope, $modalInstance, conference) {
    $scope.conference = conference;

    
    $scope.created_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };
    $scope.updated_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };

    $scope.ok = function () {
      $modalInstance.close($scope.conference);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
