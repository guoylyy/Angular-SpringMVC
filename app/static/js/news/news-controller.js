'use strict';

angular.module('news')
  .controller('NewsController', ['$scope', '$modal', 'resolvedNews', 'News',
    function ($scope, $modal, resolvedNews, News) {

      $scope.news = resolvedNews;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.news = News.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        News.delete({id: id},
          function () {
            $scope.news = News.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          News.update({id: id}, $scope.news,
            function () {
              $scope.news = News.query();
              $scope.clear();
            });
        } else {
          News.save($scope.news,
            function () {
              $scope.news = News.query();
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
          
          "is_draft": "",
          
          "publisher": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var newsSave = $modal.open({
          templateUrl: 'news-save.html',
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
