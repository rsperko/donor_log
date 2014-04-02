'use strict';

angular.module('trackingApp')
    .directive("formGroup", function() {
        return {
            template:
                '<div class="form-group" ng-class="{ error: isError }">\
                    <label for="{{for}}">{{label}}</label>\
                    <div class="controls" ng-transclude></div>\
                </div>',

            replace: true,
            transclude: true,
            require: "^form",

            scope: {
                label: '@'
            },

            link: function(scope, element, attrs, formController) {
                var input = $(element).find(":input"),
                    id = input.attr("id"),
                    name = input.attr("name");

                if(! name) {
                    input.attr("name", id);
                }

                if(! input.hasClass('form-control')) {
                    input.addClass('form-control');
                }

                scope.for = id;
                scope.label = label;

                var errorExpression = [formController.$name, name, "$invalid"].join(".");
                // Watch the parent scope, because current scope is isolated.
                scope.$parent.$watch(errorExpression, function(isError) {
                    scope.isError = isError;
                });
            }
        };
    });