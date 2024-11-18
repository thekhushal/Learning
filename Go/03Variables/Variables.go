package main

import "fmt"

func main() {
	// Variable Decleration & Initilization
	var alpha int = 1 //	1. Declearing a variable of intiger type and initializing it with a value in same line using = symbol

	var beta int //			2. Declearing a variable of string type
	beta = 1     // 			   Initilization a value to the variable in next line

	var gama = 5 //			3. Declearing a variable and initializing it with a value in same line,
	// If datatype of var is not mentined, Go Using lexur itself assigns the datatype to the variable based on the datatype of the first value initialized to it
	delta := "Delta" //		4. Declearing and initializing in same line using := syntax
	epsilon := 3     //		4. with Data Type = int
	zeta := false    //		4. with Data Type = Bool

	var eta bool = true //1 with Data type = Bool
	fmt.Println(alpha, beta, gama, delta, epsilon, zeta, eta)
	fmt.Printf("The variable is a %t /n", zeta)

	//
}
