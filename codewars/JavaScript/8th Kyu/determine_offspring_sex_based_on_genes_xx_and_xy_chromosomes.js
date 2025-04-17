// Determine offspring sex based on genes XX and XY chromosomes (8th Kyu)

/*
Task description:

The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. 
They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. 
If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. 
If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; 
If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
*/

// Define a function to determine the gender of a baby based on the sperm chromosome
// Parameter:
//   sperm - a string, either 'XY' (male) or 'XX' (female)
function chromosomeCheck(sperm) {
    // Use a ternary operator to assign 'son' if sperm is 'XY', otherwise 'daughter'
    var res = sperm == 'XY' ? "son" : "daughter";

    // Return a formatted message using template literals
    return `Congratulations! You're going to have a ${res}.`;
}