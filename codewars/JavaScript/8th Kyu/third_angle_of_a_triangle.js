// Third Angle of a Triangle (8th Kyu)

/*
Task description:

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
*/

// Define a function to calculate the third angle of a triangle
// Parameters:
//   a - first angle of the triangle
//   b - second angle of the triangle
function otherAngle(a, b) {
    // Since the sum of all internal angles in a triangle is always 180 degrees,
    // subtract the sum of the given two angles from 180 to get the third angle
    return 180 - (a + b);
}
