package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
	"strconv"
	"strings"
)

type Stack []string
type stacksMap []Stack

// IsEmpty: check if stack is empty
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

// Push a new value onto the stack
func (s *Stack) Push(str string) {
	*s = append(*s, str) // Simply append the new value to the end of the stack
}

// Remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		index := len(*s) - 1 // Get the index of the top most element.
		element := (*s)[index] // Index into the slice and obtain the element.
		*s = (*s)[:index] // Remove it from the stack by slicing it off.
		return element, true
	}
}

func (s *Stack) Peek() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		index := len(*s) - 1 // Get the index of the top most element.
		element := (*s)[index]
		return element, true
	}
}

func main() {

	var stack1 Stack
	var stack2 Stack
	var stack3 Stack
	var stack4 Stack
	var stack5 Stack
	var stack6 Stack
	var stack7 Stack
	var stack8 Stack
	var stack9 Stack

	stack1.Push("F")
	stack1.Push("C")
	stack1.Push("P")
	stack1.Push("G")
	stack1.Push("Q")
	stack1.Push("R")

	stack2.Push("W")
	stack2.Push("T")
	stack2.Push("C")
	stack2.Push("P")

	stack3.Push("B")
	stack3.Push("H")
	stack3.Push("P")
	stack3.Push("M")
	stack3.Push("C")

	stack4.Push("L")
	stack4.Push("T")
	stack4.Push("Q")
	stack4.Push("S")
	stack4.Push("M")
	stack4.Push("P")
	stack4.Push("R")

	stack5.Push("P")
	stack5.Push("H")
	stack5.Push("J")
	stack5.Push("Z")
	stack5.Push("V")
	stack5.Push("G")
	stack5.Push("N")

	stack6.Push("D")
	stack6.Push("P")
	stack6.Push("J")

	stack7.Push("L")
	stack7.Push("G")
	stack7.Push("P")
	stack7.Push("Z")
	stack7.Push("F")
	stack7.Push("J")
	stack7.Push("T")
	stack7.Push("R")

	stack8.Push("N")
	stack8.Push("L")
	stack8.Push("H")
	stack8.Push("C")
	stack8.Push("F")
	stack8.Push("P")
	stack8.Push("T")
	stack8.Push("J")

	stack9.Push("G")
	stack9.Push("V")
	stack9.Push("Z")
	stack9.Push("Q")
	stack9.Push("H")
	stack9.Push("T")
	stack9.Push("C")
	stack9.Push("W")	

	sM := stacksMap{
		stack1,
		stack2,
		stack3,
		stack4,
		stack5,
		stack6,
		stack7,
		stack8,
		stack9,
	}

	// open file
    f, err := os.Open("input-dec-5.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

    // read the file word by word using scanner
    scanner := bufio.NewScanner(f)

    var partss []string
    
    for scanner.Scan() {
    	partss = strings.Split(scanner.Text(), " ")

    	b, err := strconv.Atoi(partss[1])
    	source, err := strconv.Atoi(partss[3])
    	destination, err := strconv.Atoi(partss[5])
    	if err != nil {
    		fmt.Println("Error converting string to integer")
    	}

    	if b == 1 {
			ele, err := sM[source-1].Pop()
			if err != false {
				sM[destination-1].Push(ele)
			}
		} else {
			var stemp []string
			for i := 1; i <= b ; i++ {
    			ele, err := sM[source-1].Pop()
				if err != false {
					stemp = append(stemp, ele)
				}
    		}
    		for x := len(stemp)-1; x >= 0; x-- {
    			sM[destination-1].Push(stemp[x])
    		}
		}
    	
    	
    	
    }

    for _, val := range sM {
    	ele, err := val.Peek()
    	if err != false {
    		fmt.Print(ele)
    	}		
    }
}