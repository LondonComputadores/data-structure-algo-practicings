// package me.sekayasin;

public class Question1IsCentered {

    public static void main(String[] args) {
        System.out.println(isCentered(new int[]{3,2,1,4,1}));
    }

    static int isCentered(int[] items) {
        if (items.length == 0 || items.length % 2 == 0)
            return 0;
        int midIndex = items.length / 2;
        int middleItem = items[midIndex];
        for (int i = 0; i < items.length; i++) {
            if (i != midIndex && middleItem >= items[i])
                return 0;
        }
        return 1;
    }
}


// V2 ChatGPT Feb/2025

// public class ArrayUtils {
//     public static int isCentered(int[] arr) {
//         if (arr == null || arr.length % 2 == 0 || arr.length == 0) {
//             return 0; // No middle element
//         }

//         int midIndex = arr.length / 2;
//         int midValue = arr[midIndex];

//         for (int i = 0; i < arr.length; i++) {
//             if (i != midIndex && arr[i] <= midValue) {
//                 return 0;
//             }
//         }
//         return 1;
//     }
// }
