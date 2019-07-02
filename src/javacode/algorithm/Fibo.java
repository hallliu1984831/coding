package javacode.algorithm;

public class Fibo {
  
  public static void main(String[] args) {
    System.out.println("start fibo calculation in java");
    int count = 0,firstEle = 0,secondEle = 1,currentEle = 0,result = 0;
    result = firstEle + secondEle;
    int arg = Integer.valueOf(args[0]).intValue();
    for (int i = 0; i < arg; i++) {
      currentEle = firstEle + secondEle;
      result += currentEle;
      firstEle = secondEle;
      secondEle = currentEle;
    }
    System.out.println("fibo number is:" + currentEle + " and calculation result is:" + result);
  }
}
