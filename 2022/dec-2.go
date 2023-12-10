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
    f, err := os.Open("input-dec-2.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

    // read the file word by word using scanner
    scanner := bufio.NewScanner(f)
    //scanner.Split(bufio.ScanWords)
    a := "C"
    b := "D"
    var c []string
    total := 0

    for scanner.Scan() {
        // do something with a word
        a = scanner.Text()
        c = strings.Split(a, " ")

        a = c[0]
        b = c[1]

        if b == "X" {

        	switch a {
        	case "A":
        		total += 3
        	case "B":
        		total += 1
        	case "C":
        		total += 2
        	default:
        	}
        } else if b == "Y" {
        	total += 3

        	switch a {
        	case "A":
        		total += 1
        	case "B":
        		total += 2
        	case "C":
        		total += 3
        	default:
        		//return
        	}
        } else {
        	total += 6

        	switch a {
        	case "A":
        		total += 2
        	case "B":
        		total += 3
        	case "C":
        		total += 1
        	default:
        		//return
        	}
        }
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

    fmt.Println(total)
}