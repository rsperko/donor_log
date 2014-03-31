'use strict';

angular.module('trackingApp')
    .directive("controlGroup", function() {
    return {
        template:
            '<div class="control-group" ng-class="{ error: isError }">\
                <label class="control-label" for="{{for}}">{{label}}</label>\
                <div class="controls" ng-transclude></div>\
            </div>',

        replace: true,
        transclude: true,
        require: "^form",

        scope: {
            label: "@", // Gets the string contents of the `label` attribute.
            cols: "@"
        },

        link: function(scope, element, attrs, formController) {
            // The <label> should have a `for` attribute that links it to the input.
            // Get the `id` attribute from the input element
            // and add it to the scope so our template can access it.
            var id = element.find(":input").attr("id");
            scope.for = id;

            scope.col_class = ''
            if(scope.cols) {
                scope.col_class = 'col-md-' + cols;
            }

            // Get the `name` attribute of the input
            var inputName = element.find(":input").attr("name");
            // Build the scope expression that contains the validation status.
            // e.g. "form.example.$invalid"
            var errorExpression = [formController.$name, inputName, "$invalid"].join(".");
            // Watch the parent scope, because current scope is isolated.
            scope.$parent.$watch(errorExpression, function(isError) {
                scope.isError = isError;
            });
        }
    };
});