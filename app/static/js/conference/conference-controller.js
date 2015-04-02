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
          $scope.clear();
          $scope.open("", true);
      };

      function countActiveConference() {
       
        for (var i = 0; i < $scope.conferences.length; i++) {
          if ($scope.conferences[i].is_show_android) {
            return $scope.conferences[i];
            break;
          }
        };
        return null;
      };

      function countInTimeConference() {
        for (var i = 0; i < $scope.conferences.length; i++) {
          if($scope.conferences[i].is_show_in_time){
            return $scope.conferences[i];
            break;
          }
        };
        return null;
      };


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

          "group_content": "",

          "layout_content": "",

          "agenda_content": "",

          "title": "",

          "created_time": "",

          "updated_time": "",

          "started_time": "",

          "view_count": "",

          "is_draft": false,

          "is_show_android" : false,

          "is_show_ios" : false,

          "is_show_in_time": false,

          "id": ""
        };
      };

      $scope.open = function(id, is_create) {
        var base_url = "views/conference/";
        if (is_create) {
          base_url = base_url + "conference-add.html";
        } else {
          base_url = base_url + "conference-update.html";
        }
        var conferenceSave = $modal.open({
          templateUrl: base_url,
          controller: ConferenceSaveController,
          resolve: {
            conference: function() {
              var entity = {
                'conference':$scope.conference,
                'android_active_count':countActiveConference(),
                'in_time_count':countInTimeConference()
              };
              return entity;
            }
          }
        });

        conferenceSave.result.then(function(entity) {
          $scope.conference = entity;
          $scope.save(id);
          $scope.conferences = resolvedConference;
        });
      };
    }
  ]);

var ConferenceSaveController =
  function($scope, $modalInstance, conference, $filter, $upload, $http) {
    $scope.conference = conference.conference;
    $scope.android_active_count = conference.android_active_count;
    $scope.in_time_count = conference.in_time_count;
    $scope.requested_pdf = false;
    $scope.pdfs = [];
    //request the list of conference pdf
    if ($scope.conference.id != undefined && !$scope.requested_pdf) {
      $scope.requested_pdf == true;
      request_pdf();
    };

    $scope.$watch(function() {
        return $scope.conference.id;
      },
      function(newValue, oldValue) {
        if(oldValue == undefined && newValue != undefined && $scope.requested_pdf == false){
          request_pdf();
        }
    });

    function request_pdf() {
      $http.get('news/conferences/' + $scope.conference.id + '/get_file/PDF')
        .success(function(data) {
          $scope.pdfs = data;
        })
        .error(function() {});
    };

    $scope.delete_pdf = function(id){
      $http.post('/news/conferences/file/'+id)
        .success(function(data){
          request_pdf();
        })
        .error(function(data){
          alert('删除失败！');
        });
    };

    $scope.uploadFile = function(key, fx, event) {
      var file = fx[0];
      if (key == 'pdf') {
        $upload.upload({
          url: '/news/conferences/' + $scope.conference.id + '/file_upload/PDF',
          file: file
        }).progress(function(evt) {}).success(function(data, status, headers, config) {
          console.log('success');
          request_pdf();
        });
      } else {
        $upload.upload({
          url: 'news/upload_image',
          file: file
        }).progress(function(evt) {}).success(function(data, status, headers, config) {
          console.log('success');
          alert('上传成功！');
          $scope.conference[key] = $scope.conference[key] + getImageHTML(data.path);
        });
      }
    };

    function getImageHTML(path) {
      return '<img src="' + path + '" width="100%"></img>';
    }

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
      if($scope.android_active_count != null && $scope.conference.is_show_android == true &&
        $scope.android_active_count.id != $scope.conference.id){
        alert('安卓设备只支持一个会议，请设置安卓设备为隐藏再保存！');
      }else if($scope.in_time_count != null && $scope.conference.is_show_in_time == true &&
        $scope.in_time_count.id != $scope.conference.id){
        alert('已经有一个作为倒计时的会议拉！请关闭倒计时选项！');
      }else{
        $modalInstance.close($scope.conference);
      }
    };

    $scope.cancel = function() {
      $modalInstance.dismiss('cancel');
    };
  };