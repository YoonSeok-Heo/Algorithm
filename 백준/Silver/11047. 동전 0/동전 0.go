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
	scanner.Split(bufio.ScanWords)

	answer := 0
	var N, K int

	N = scanInt()
	K = scanInt()

	coinLst := make([]int, N)

	for i := 0; i < N; i++ {
		coinLst[i] = scanInt()
	}

	for i := N - 1; i >= 0; i-- {
		answer += K / coinLst[i]
		K = K % coinLst[i]
	}

	fmt.Fprint(writer, answer)
}

func scanInt() int {
	scanner.Scan()
	s, _ := strconv.Atoi(scanner.Text())
	return s
}
