package main
import (
  "fmt"
  "io"
  "os"
)

func main() {
  count, firstEle, secondEle, currentEle, result := 0, 0, 1, 0, 0
  result = firstEle + secondEle
  fmt.Println("please input fibo number:")
  _, err  := fmt.Scan(&count)
  _ = err
  for i := 0; i < count; i++ {
    currentEle = firstEle + secondEle
    fmt.Println(currentEle)
    result += currentEle
    firstEle = secondEle
    secondEle = currentEle
    _ = result
    _ = firstEle
    _ = secondEle
  }
  s := fmt.Sprintln("fibo result is", currentEle, "and calculation result is", result)
  io.WriteString(os.Stdout, s)
}

