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

func init() {
	scanner.Split(bufio.ScanWords)
}

func scanInt() int {
	scanner.Scan()
	s, _ := strconv.Atoi(scanner.Text())
	return s
}

func main() {
	defer writer.Flush()

	answer, end := 0, 0
	N := scanInt()

	slc := make([][]int, N)

	for i := 0; i < N; i++ {
		tmp := []int{scanInt(), scanInt()}
		slc[i] = tmp
	}

	sort.Slice(slc, func(i, j int) bool {
		return slc[i][0] < slc[j][0]
	})

	sort.Slice(slc, func(i, j int) bool {
		return slc[i][1] < slc[j][1]
	})

	for _, value := range slc {
		if end <= value[0] {
			answer++
			end = value[1]
			//fmt.Println(value)
		}
		//fmt.Fprint(writer, value)
	}

	fmt.Fprint(writer, answer)

}
