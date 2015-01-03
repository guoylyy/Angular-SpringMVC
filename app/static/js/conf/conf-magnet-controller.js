'use strict';

angular.module('news')
  .controller('MagnetConfController', ['$scope', '$modal','$upload', '$http',
    function ($scope, $modal, $upload, $http) {
    	
    	$scope.generateThumb = function(){
    		var file = $scope.picFile[0];
    		$upload.upload({
    			url:'news/mockimage',
    			data: {myObj: $scope.myModelObj},
    			file:file
    		}).progress(function(evt) {
     		 }).success(function(data, status, headers, config) {
       			 console.log('success');
             alert('上传成功！');
             load();
      		});
    	};

      function load(){
        $http.get('/news/mockimage').
          success(function(data){
            $scope.entity = data;
          }).
          error(function(data){
            console.log('error happen');
          });
      };
      load();

    }]);
