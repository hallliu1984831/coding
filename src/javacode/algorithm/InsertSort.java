package javacode.algorithm;

import java.util.Arrays;

public class InsertSort {
    public static void main(String[] args) {
        int[] randomNumberArray = {6, 5, 7, 9, 2, 3, 8, 4};
        int arrayLength = randomNumberArray.length;
        int[] result = new int[arrayLength];
        System.out.println("The number array content before sort");
        System.out.println(Arrays.toString(randomNumberArray));

        result[0] = randomNumberArray[0];
        for (int startIndex = 1; startIndex < arrayLength; startIndex++) {
            for (int insertIndex = startIndex - 1; insertIndex >= 0; insertIndex--) {
                int temp = 0;
                if (result[insertIndex] > randomNumberArray[startIndex]) {
                    temp = result[insertIndex];
                    result[insertIndex] = randomNumberArray[startIndex];
                    result[startIndex] = temp;
                } else {
		    result[startIndex] = randomNumberArray[startIndex];
		    break;
                }
            }
        }
        System.out.println("The number array content after sort from low to high");
        System.out.println(Arrays.toString(result));
    }
}
