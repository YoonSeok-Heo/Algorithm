package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	scanner.Buffer(make([]byte, 0, 2000000), 2000000)

	answer := 0

	N, M := scanInt(), scanInt()
	is := scanString()
	i, count := 0, 0
	for i < M-2 {
		if is[i:i+3] == "IOI" {
			count++
			i += 2
			if count == N {
				answer++
				count--
			}
		} else {
			i++
			count = 0
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
