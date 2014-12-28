'use strict';

angular.module('news')
  .controller('NewsController', ['$scope', '$modal', 'resolvedNews', 'News',
    function ($scope, $modal, resolvedNews, News) {

      $scope.newses = resolvedNews;

      $scope.editorOptions = {
        language: 'ru',
        uiColor: '#000000'
      };

      $scope.create = function () {
        $scope.clear();
        $scope.open(undefined,true);
      };

      $scope.update = function (id) {
        $scope.news = News.get({id: id});
        $scope.open(id, false);
      };

      $scope.delete = function (id) {
        News.delete({id: id},
          function () {
            $scope.newses = News.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          News.update({id: id}, $scope.news,
            function () {
              $scope.newses = News.query();
              $scope.clear();
            });
        } else {
          News.save($scope.news,
            function () {
              $scope.newses = News.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.news = {
          
          "title": "",
          
          "content": "",
          
          "create_time": "",
          
          "update_time": "",
          
          "author": "",
          
          "view_count": "",
          
          "is_draft": false,
          
          "id": ""
        };
      };

      $scope.open = function (id, is_create) {
        var template = "views/news/";
        if (is_create) {
          template = template + "news-add.html";
        }else{
          template = template + "news-update.html";
        }
        var newsSave = $modal.open({
          templateUrl: template,
          controller: NewsSaveController,
          resolve: {
            news: function () {
              return $scope.news;
            }
          }
        });

        newsSave.result.then(function (entity) {
          $scope.news = entity;
          $scope.save(id);
        });
      };
    }]);

 var NewsSaveController =
  function ($scope, $modalInstance, news) {
    $scope.news = news;

    $scope.create_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
    };
    $scope.update_timeDateOptions = {
      dateFormat: 'yy-mm-dd',
    };

    $scope.ok = function () {
      $modalInstance.close($scope.news);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
