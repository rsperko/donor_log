'use strict';

describe('Factory: EntityModel', function () {

  // load the controller's module
  beforeEach(module('trackingApp'));

  var model;

  // Initialize the controller and a mock scope
  beforeEach(inject(function (entityModel) {
    model = entityModel();

  }));

  it('set the primary phone', function() {
    model.phones = [
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
    ];

    expect(model.phones.length).toBe(3);
    expect(model.phones[1].primary).toBe(true);

    model.primaryPhone(2);

    expect(model.phones[1].primary).toBe(false);
    expect(model.phones[2].primary).toBe(true);
  });
});
