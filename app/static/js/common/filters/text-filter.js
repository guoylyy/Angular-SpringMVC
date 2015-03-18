angular.module('news').filter("timeFilter", function() {
  return function(error) {
    return 'sfasfsa';
  };
}).filter('DraftFilter', function(){
	/*
		安卓设备的回忆为 false，则代表不是 draft
	 */
	return function(input){
		if(input){
			return '否';
		}else{
			return '是';
		}
	};
}).filter('deviceFilter', function(){
	/*
		安卓设备的回忆为 false，则代表不是 draft
	 */
	return function(input){
		if(input){
			return '是';
		}else{
			return '否';
		}
	};
});