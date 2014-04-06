'use strict';

describe('Controller: EntityCtrl', function () {

  // load the controller's module
  beforeEach(module('trackingApp'));

  var EntityCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();

    scope.model = {
      phones: [
        {
          primary: false,
          number: '414-444-4444',
          type: 'M'
        },
        {
          primary: true,
          number: '414-444-4445',
          type: 'M'
        },
        {
          primary: false,
          number: '414-444-4446',
          type: 'M'
        }
      ]
    };

    EntityCtrl = $controller('EntityCtrl', {
      $scope: scope
    });
    EntityCtrl.setupEntityActions();
  }));

  it('deleting primary phone causes first phone to be primary', function () {
    expect(scope.model.phones.length).toBe(3);

    scope.deletePhone(1);

    expect(scope.model.phones.length).toBe(2);
    expect(scope.model.phones[0].primary).toBe(true);
  });
});
