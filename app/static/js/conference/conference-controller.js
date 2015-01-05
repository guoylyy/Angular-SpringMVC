'use strict';

angular.module('news')
  .controller('ConferenceController', ['$scope', '$modal', 'resolvedConference', 'Conference',
    function($scope, $modal, resolvedConference, Conference) {

      $scope.conferences = resolvedConference;
      //配置ckeditor
      $scope.editorOptions = {
        language: 'ru',
        uiColor: '#000000'
      };

      $scope.editorOptions = {
        language: 'ru',
        uiColor: '#000000'
      };
      $scope.create = function() {
        if(countActiveConference() >= 1){
          alert('已经有一个激活的会议内容了！');
        }else{
          $scope.clear();
          $scope.open("",true);
        }
      };

      function countActiveConference(){
        var count = 0;
        for (var i = 0; i < $scope.conferences.length; i++) {
          if(!$scope.conferences[i].is_draft){
            count++;
          }
        };
        return count;
      }

      $scope.update = function(id) {
        $scope.conference = Conference.get({
          id: id
        });
        $scope.open(id, false);
      };

      $scope.delete = function(id) {
        Conference.delete({
            id: id
          },
          function() {
            $scope.conferences = Conference.query();
          });
      };

      $scope.save = function(id) {
        if (id) {
          Conference.update({
              id: id
            }, $scope.conference,
            function() {
              $scope.conferences = Conference.query();
              $scope.clear();
            });
        } else {
          Conference.save($scope.conference,
            function() {
              $scope.conferences = Conference.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function() {
        $scope.conference = {

          "intro_content": "",

          "logistics_content": "",

          "group_content":"",

          "layout_content": "",

          "agenda_content" :"",

          "title": "",

          "created_time": "",

          "updated_time": "",

          "started_time": "",

          "view_count": "",

          "is_draft": false,

          "id": ""
        };
      };

      $scope.open = function(id, is_create) {
        var base_url = "views/conference/";
        if(is_create){
          base_url = base_url + "conference-add.html";
        }else{
          base_url = base_url + "conference-update.html";
        }
        var conferenceSave = $modal.open({
          templateUrl: base_url,
          controller: ConferenceSaveController,
          resolve: {
            conference: function() {
              return $scope.conference;
            }
          }
        });

        conferenceSave.result.then(function(entity) {
          $scope.conference = entity;
          $scope.save(id);
        });
      };
    }
  ]);

var ConferenceSaveController =
  function($scope, $modalInstance, conference, $filter) {
  $scope.conference = conference;
  $scope.created_timeDateOptions = {
    dateFormat: 'yy-mm-dd',
  };
  $scope.updated_timeDateOptions = {
    dateFormat: 'yy-mm-dd',
  };
  $scope.started_timeDateOptions = {
    dateFormat: 'yy-mm-dd',
  };

  $scope.$watch(function() {
      return $scope.conference.started_time;
    },
    function(newValue, oldValue) {
      if (newValue != undefined && newValue.indexOf('T') > -1) {
        $scope.conference.started_time = $filter('date')(newValue,
          'yyyy-MM-dd HH:mm:ss');
      };
    });

  $scope.onTimeSet = function(newDate, oldDate) {
    $scope.conference.started_time = $filter('date')(newDate,
      'yyyy-MM-dd HH:mm:ss');
  };

  $scope.ok = function() {
    $modalInstance.close($scope.conference);
  };

  $scope.cancel = function() {
    $modalInstance.dismiss('cancel');
  };
};