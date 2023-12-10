package main

import (
	"bufio"
    "fmt"
    "log"
    "os"
    "strings"
)

func main() {

	// open file
    f, err := os.Open("input-dec-3.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

    // read the file word by word using scanner
    scanner := bufio.NewScanner(f)

    total := 0
    num := 0
    var bags [3]string
    counter := 0
    first := ""
    second := ""
    third := ""
    seen := ""
    for scanner.Scan() {
    	bags[counter] = scanner.Text()
    	counter++

    	if counter == 3 {

    		counter = 0
    		first = bags[0] 
    		second = bags[1]
    		third = bags[2]

    		for _, letter := range first {
	        	if strings.Contains(second, string(letter)) && strings.Contains(third, string(letter)) {
	        		if !strings.Contains(seen, string(letter)) {
	        			seen += string(letter)
	        			num = int(letter)
	        			// check if lowercase
	        			if num >= 97 && num <= 122 {
	        				total += (num - 96)
	        			} else {
	        				total += (num - 64) + (26)
	        			}
        			}
	        	}
    		}
    		seen = ""
    	}
    }

    if counter == 3 {

		counter = 0
		first = bags[0] 
		second = bags[1]
		third = bags[2]

		for _, letter := range first {
        	if strings.Contains(second, string(letter)) && strings.Contains(third, string(letter)) {
    			num = int(letter)
    			// check if lowercase
    			if num >= 97 && num <= 122 {
    				total += (num - 96)
    			} else {
    				total += (num - 64) + (26)
    			}
        	}
		}
	}

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Println(total)
}
