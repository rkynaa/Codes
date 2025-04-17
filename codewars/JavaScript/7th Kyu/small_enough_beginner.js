// Small enough? - Beginner (7th Kyu)

/*
Task description:

You will be given an array and a limit value. 
You must check that all values in the array are below or equal to the limit value. 
If they are, return true. Else, return false.

You can assume all values in the array are numbers.
*/

// Define a function to check if all elements in an array are less than or equal to a given limit
// Parameters:
//   a     - an array of numbers
//   limit - the maximum allowed value
function smallEnough(a, limit) {
    var count = true;  // Assume all values are within the limit by default

    // Loop through each element in the array
    for (i = 0; i < a.length; i++) {
        // If any element is greater than the limit, set count to false
        if (a[i] > limit) {
            count = false;
        }
    }

    // Return true if all elements are within the limit, otherwise false
    return count;
}