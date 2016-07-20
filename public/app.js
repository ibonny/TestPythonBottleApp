/* global angular */

angular.module('myApp', [])
    .controller('myController', ['$scope', '$http', '$sce', function($scope, $http, $sce) {
        $scope.variable = "Testout";
        
        $scope.doSomething = function() {
            $scope.result = "Done something.";
        };
        
        $scope.clearIt = function() {
            $scope.result = "";
        };
        
        $scope.getDirectory = function() {
            $http.get('/getDirectory').then(function success(data) {
                $scope.result = "<pre>" + data.data + "</pre>";
            }, function error(data) {
                $scope.result = "ERROR"; 
            });
        };
        
    }])
    .filter("sanitize", ['$sce', function($sce) {
        return function(htmlCode){
            return $sce.trustAsHtml(htmlCode);
        };
    }]);
