package javacode.algorithm;

import java.util.Arrays;

public class InsertSort {
    public static void main(String[] args) {
        int[] randomNumberArray = {6, 5, 7, 9, 2, 3, 8, 4};
        System.out.println("The number array content before sort");
        System.out.println(Arrays.toString(randomNumberArray));
        int arrayLength = randomNumberArray.length;
        int temp = 0;
        for (int startIndex = 1; startIndex < arrayLength; startIndex++) {
            for (int insertIndex = 0; insertIndex < startIndex; insertIndex++) {
                if (randomNumberArray[startIndex] > randomNumberArray[insertIndex]) {
                    temp = randomNumberArray[startIndex];
                    randomNumberArray[startIndex] = randomNumberArray[insertIndex];
                    randomNumberArray[insertIndex] = temp;
                    break;
                }
            }
        }
        System.out.println("The number array content after sort from low to high");
        System.out.println(Arrays.toString(randomNumberArray));
    }
}