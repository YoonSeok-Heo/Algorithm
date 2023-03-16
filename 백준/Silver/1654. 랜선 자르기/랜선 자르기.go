package main
import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

var (
	s = bufio.NewScanner(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	
)

func main(){
	defer w.Flush()
	s.Split(bufio.ScanWords)
	N, M := scanInt(), scanInt()
	
	lst := make([]int, N)
	
	var maxH int = 0
	var tmp int
	for i:=0; i < N; i++{
		tmp = scanInt()
		lst[i] = tmp
		if tmp > maxH{
			maxH = tmp
		}
	}
	
	var left, right, mid int = 1, maxH, 0
	
	for left <= right{
		mid = (left + right) / 2
		count := 0
		for i:=0; i < N; i++{
			count += lst[i] / mid
		}
		if count >= M{
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	fmt.Fprint(w, right)
}

func scanInt() int {
	s.Scan()
	n, _ := strconv.Atoi(s.Text())
	return n
}