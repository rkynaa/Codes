// Multiplication table for number (8th Kyu)

/*
Task description:

Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50

P. S. You can use \n in string to jump to the next line.

Note: newlines should be added between rows, but there should be no trailing newline at the end. 
If you're unsure about the format, look at the sample tests.
*/

// Define a function to generate a multiplication table for a given number (1 to 10)
function multiTable(number) {
    var res = "";  // Initialize an empty string to accumulate the result

    // Loop from 1 through 10 (inclusive)
    for (i = 1; i != 11; i++) {
        // Construct the current line of the multiplication table:
        // e.g., "1 * 5 = 5"
        res += i.toString() + " * " + number.toString() + " = " + String(i * number);

        // Add a newline character after each line except the last one
        if (i != 10) {
            res += "\n";
        }
    }

    // Return the complete formatted multiplication table as a string
    return res;
}