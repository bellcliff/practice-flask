(function() {

    'use strict';

    angular.module('flask', []).controller('myCtrl', function($http) {
        var self = this;
        self.name = "World";

        $http.get('/api/user').then(function(data) {
            self.users = data.data;
        });
    });

})();
