// Factorial (7th Kyu)

/*
Task description:

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. 
If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

More details about factorial can be found here.
*/

// Define a function to compute the factorial of a number n
function factorial(n) {
    console.log(n); // Log the input value to the console for debugging purposes
  
    // Check if the input is outside the allowed range (0 to 12)
    // If so, throw a RangeError to indicate invalid input
    if (n < 0 || n > 12) {
      throw new RangeError("The argument must be in positive numbers!");
    }
  
    // If n is 0, by definition factorial(0) is 1
    if (n == 0) {
      n = 1;
    }
  
    var res = 1; // Initialize result variable to store the factorial value
  
    // Loop from n down to 1, multiplying each number into the result
    for (i = n; i > 0; i--) {
      res = res * i;
    }
  
    // Return the computed factorial value
    return res;
  }  