package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	answer := 0

	N, M := scanInt(), scanInt()
	inputString := scanString()

	searchWord := "I" + strings.Repeat("OI", N)
	//fmt.Fprintln(writer, "N", N)
	//fmt.Fprintln(writer, "M", M)
	//fmt.Fprintln(writer, inputString)
	//fmt.Fprintln(writer, searchWord)

	var flag bool
	for i := 0; i <= M-(1+(2*N)); i++ {
		flag = true
		//fmt.Fprintln(writer, i)
		//fmt.Fprintln(writer, inputString[i])
		for j := 0; j < 1+(2*N); j++ {
			if searchWord[j] == inputString[i+j] {
				continue
			}
			flag = false
			break
		}
		if flag {
			answer++
		}
	}
	fmt.Fprintln(writer, answer)
}
func scanInt() int {
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	return n
}

func scanString() string {
	scanner.Scan()
	s := scanner.Text()
	return s
}
