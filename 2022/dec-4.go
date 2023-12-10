package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
	"strconv"
	"strings"
)

func main() {
	// open file
    f, err := os.Open("input-dec-4.txt")
    if err != nil {
        log.Fatal(err)
    }
    // remember to close the file at the end of the program
    defer f.Close()

    // read the file word by word using scanner
    scanner := bufio.NewScanner(f)

    total := 0
    var partss []string
    var parts1 []string
    var parts2 []string

    for scanner.Scan() {
    	partss = strings.Split(scanner.Text(), ",")
    	parts1 = strings.Split(partss[0], "-")
    	parts2 = strings.Split(partss[1], "-")

    	a, err := strconv.Atoi(parts1[0])
    	b, err := strconv.Atoi(parts1[1])
    	c, err := strconv.Atoi(parts2[0])
    	d, err := strconv.Atoi(parts2[1])

    	if a == c || (a > c && a <= d) || b == d || (b >= c && b < d) {
    		total++
    	} else if c == a || (c > a && c <= b) || b == d || (d >= a && d < b) {
    		total++
    	}

    	if err != nil {
    		fmt.Println("Errorrrr")
    	}

    }

    fmt.Println(total)

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
