package main

import (
	"flag"
	"fmt"
)

var name string

func init() {
  flag.StringVar(&name, "name", "robot", "Robot object" )
}

func main() {
  flag.Parse()
  fmt.Printf("Hello %s\n", name)
}
