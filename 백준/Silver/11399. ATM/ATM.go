package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	N := scanInt()

	slc := make([]int, N)

	for i := 0; i < N; i++ {
		slc[i] = scanInt()
	}

	sort.Sort(sort.Reverse(sort.IntSlice(slc)))

	for i := 0; i < N; i++ {
		answer += slc[i] * (i + 1)
	}
	fmt.Fprint(writer, answer)
}

func scanInt() int {
	scanner.Scan()
	ret, _ := strconv.Atoi(scanner.Text())
	return ret
}
