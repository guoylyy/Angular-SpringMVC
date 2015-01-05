'use strict';

angular.module('news')
  .controller('MovieController', ['$scope', '$modal', 'resolvedMovie', 'Movie',
    function ($scope, $modal, resolvedMovie, Movie) {

      $scope.movies = resolvedMovie;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.movie = Movie.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Movie.delete({id: id},
          function () {
            $scope.movies = Movie.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Movie.update({id: id}, $scope.movie,
            function () {
              $scope.movies = Movie.query();
              $scope.clear();
            });
        } else {
          Movie.save($scope.movie,
            function () {
              $scope.movies = Movie.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.movie = {
          
          "name": "",
          
          "url": "",
          
          "size": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var movieSave = $modal.open({
          templateUrl: 'movie-save.html',
          controller: MovieSaveController,
          resolve: {
            movie: function () {
              return $scope.movie;
            }
          }
        });

        movieSave.result.then(function (entity) {
          $scope.movie = entity;
          $scope.save(id);
        });
      };
    }]);

var MovieSaveController =
  function ($scope, $modalInstance, movie, $upload) {
    $scope.movie = movie;
    $scope.uploadFile = function(fx,event) {
      var file = fx[0];
      $scope.movie.size = parseFloat((file.size/1024)/2014).toFixed(2);
      $upload.upload({
        url: 'news/upload_image',
        file: file
      }).progress(function(evt) {}).success(function(data, status, headers, config) {
        console.log('success');
        alert('上传成功！');
        $scope.movie.url = data.path;
      });
    };
    
    $scope.ok = function () {
      $modalInstance.close($scope.movie);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
