'use strict';

angular.module('news')
	.directive('header', function() {
		return {
			templateUrl: 'views/common/header.html',
			restrict: 'E',
			controller: function($scope, $sessionStorage, $localStorage, $location, inform) {
				var error_conf = {
					ttl: 4000,
					type: 'default'
				};
				if ($localStorage.token == undefined || $localStorage.token.length == 0) {
					$location.url('login');
					inform.add('请登录！', error_conf);
				}
				$scope.logout = function() {
					$localStorage.token = undefined;
					$location.url('/login');
				};
			}
		};
	}).directive('ngConfirmClick', [
		function() {
			return {
				priority: -1,
				restrict: 'A',
				link: function(scope, element, attrs) {
					element.bind('click', function(e) {
						var message = attrs.ngConfirmClick;
						if (message && !confirm(message)) {
							e.stopImmediatePropagation();
							e.preventDefault();
						}
					});
				}
			}
		}
	]);;