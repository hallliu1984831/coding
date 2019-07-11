package javacode.algorithm;

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] randomNumberArray = {6, 5, 7, 9, 2, 3, 8, 4};
        System.out.println("The number array content before sort");
        System.out.println(Arrays.toString(randomNumberArray));

        int arrayLength = randomNumberArray.length;
        int tempNumber = 0;
        for (int outerIndex = 0; outerIndex < arrayLength -1; outerIndex++) {
            for (int innerIndex = outerIndex + 1; innerIndex < arrayLength; innerIndex++) {
                if (randomNumberArray[outerIndex] > randomNumberArray[innerIndex]) {
                    tempNumber = randomNumberArray[outerIndex];
                    randomNumberArray[outerIndex] = randomNumberArray[innerIndex];
                    randomNumberArray[innerIndex] = tempNumber;
                }
            }
        }
        System.out.println("The number array content after sort from low to high");
        
        System.out.println(Arrays.toString(randomNumberArray));
    }
}