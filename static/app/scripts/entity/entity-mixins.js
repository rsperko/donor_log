'use strict';

function EntityControllerMixin($scope, alert) {
    var self = this;

    self.setupEntityActions = function() {
        $scope.save = function() {
            $scope.model.save().then(function(result) {
                alert.add("success", "Saved successfully");
            },
            function(error) {
                alert.add("danger", "Failed to save " + angular.toJson(error.data));
            });
        };

        $scope.addPhone = function() {
            $scope.model.newPhone();
        };

        $scope.deletePhone = function(phoneIndex) {
            var deleted = $scope.model.phones.splice(phoneIndex, 1);
            if(deleted.primary && $scope.model.phones.length) {
                $scope.model.phones[0].primary = true;
            }
        };

        $scope.primaryPhone = function(phoneIndex) {
            _.each($scope.model.phones, function(phone, index) {
                phone.primary = index === phoneIndex;
            });
        };

        $scope.createCommunication = function() {
            $scope.newCommunication = $scope.model.createCommunication();
        };

        $scope.saveNewCommunication = function() {
            $scope.model.addCommunication($scope.newCommunication);
            $scope.newCommunication = null;
        };

        $scope.cancelNewCommunication = function() {
            $scope.newCommunication = null;
        };

        $scope.deleteCommunication = function(communicationIndex) {
            $scope.model.deleteCommunication($scope.model.communications[communicationIndex]);
        };
    };
}

EntityControllerMixin.prototype.apply = function(target) {
    _.extend(target, this);
};