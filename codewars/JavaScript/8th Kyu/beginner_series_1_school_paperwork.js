// Beginner Series #1 School Paperwork (8th Kyu)

/* 
Task description:

Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:

n= 5, m=5: 25
n=-5, m=5:  0

Waiting for translations and Feedback! Thanks!
*/

// Define a function to calculate the total number of pages needed for paperwork
// Parameters:
//   n - number of classmates
//   m - number of pages each classmate needs
function paperwork(n, m) {
    // If either value is negative, return 0 (no negative pages or classmates allowed)
    if (n < 0 || m < 0) {
        return 0;
    } else {
        // Otherwise, return the total number of pages: n classmates * m pages each
        return n * m;
    }
}