angular.module('news')
  .controller('LoginController',
    	function ($scope, $modal, $upload, $http, $location, inform, $localStorage) {
			$scope.username = undefined;
			$scope.password = undefined;

			var error_conf = {
    			ttl: 4000, type: 'default'
    		};
    		$scope.$storage = $localStorage.$default({token:''});
			$scope.submit = function() {
				console.log($scope.username);
				$http({
					url: 'news/admin_login',
					method: 'POST',
					data: {
						'account': $scope.username,
						'password': $scope.password
					}
				}).then(function(data) {
					$localStorage.token = data.data.token;
					$location.url('/');
				}, function(data) {
					inform.add('账号或密码错误！',error_conf);
				});
			};
		});