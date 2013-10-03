/**
 * Created with PyCharm.
 * User: nathan
 * Date: 10/3/13
 * Time: 10:55 AM
 * To change this template use File | Settings | File Templates.
 */

app = angular.module('ColonyCounter', []);

function MainController($scope) {
    $scope.modes = {
        CAMERA: 0,
        SETTINGS: 1
    };

    $scope.show = $scope.modes.CAMERA;

    $scope.takePicture = function () {
        $scope.show = $scope.modes.SETTINGS;
    }

}