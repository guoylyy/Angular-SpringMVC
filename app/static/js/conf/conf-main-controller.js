'use strict';

angular.module('news')
  .controller('MainConfController', ['$scope', '$modal', '$http', '$upload',
    function ($scope, $modal, $http ,$upload) {
    	$scope.idd = 1;
    	function load_entities(){
    		$http.get('news/mainpage_images').
    			success(function(data){
    				$scope.entities = data;
    			}).
    			error(function(data){
    				alert('未知错误');
    			});
    	};

    	function load_news(){
    		$http.get('news/news').
    			success(function(data){
    				$scope.newses = data;
    			}).
    			error(function(data){
    				alert('未知错误');
    			});
    	};


    	$scope.generateThumb = function(id, fx, event){
    		var file = fx[0];
    		$upload.upload({
    			url:'news/update_mainpage_image/'+id,
    			file:file
    		}).progress(function(evt) {
     		 }).success(function(data, status, headers, config) {
       			 console.log('success');
             	 alert('上传成功！');
             	 load_entities();
    			 load_news();
      		});
    	};


    	$scope.update_news = function(entity){
    		$http({
    			url:'news/update_news_link/'+entity.id,
    			method: 'POST',
    			data:{'news_id':entity.news_id}
    		}).then(function(data){
    			console.log(data);
    		}, function(data){

    		});
    	};

    	$scope.clear_files = function(){
    		$scope.picFile = [];
    	}


    	load_entities();
    	load_news();

    }]);
