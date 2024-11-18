package main

import "fmt"

func main() {
	// Operators with string
	fmt.Println("go" + "lang")

	fmt.Println("go" == "lang")
	fmt.Println("go" != "lang")
	// TODO
	fmt.Print("len(\"golang\") = ", len("golang")) // len("golang") = 61 + 1 =  2 once this outcome came  fnd why this came, it dosent come now, eventhough code is same

	fmt.Println("")
	// Operators with int and float
	fmt.Println("1 + 1 = ", 1+1)
	fmt.Println("7.5/ 3.2 = ", 7.5/3.2)

	// Operators with boolean
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}
