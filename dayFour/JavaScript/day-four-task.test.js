const { sumOfTwoNumbers, rangeBetweenLargestAndSmallestNumbers } = require('./day-four-task.js');

test('test that sum of two numbers gives the correct value', () => {
    expect(sumOfTwoNumbers([ 8, 6, 12, 4, -2 ], 6)).toStrictEqual([ 8, -2 ]);
});

test('test that the range between the largest and smallest return the correct value', () => {
    expect(rangeBetweenLargestAndSmallestNumbers([14, 9, 6, 5, 8, 10]).toStrictEqual([5, 6, 7, 8, 9, 10, 11, 12, 13, 14]));
});
