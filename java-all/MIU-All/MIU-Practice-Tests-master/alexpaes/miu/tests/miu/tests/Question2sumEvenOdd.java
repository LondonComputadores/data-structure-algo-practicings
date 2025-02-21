package miu.tests;

public class Question2sumEvenOdd {

    // public static void main(String[] args) {
    //     System.out.println(sumEvenOdd(new int[]{1,2,3,4}));
    // }

    public static int sumEvenOdd(int[] items) {
        int sumEven = 0;
        int sumOdd = 0;

        for (int i = 0; i < items.length; i++) {
            if (items[i] % 2 == 0)
                sumEven += items[i];
            else
                sumOdd += items[i];
        }
        return sumOdd - sumEven;
    }

    public int[] sumOdd;
    public Object sumEven;
}

// --------------------------------------------------------

// V2 ChatGPT Feb/2025 // funfa ok

// package miu.tests;

// public class Question2sumEvenOdd {

//     public static int sumEvenOdd(int[] items) {
//         int sumEven = 0;
//         int sumOdd = 0;

//         for (int item : items) {
//             if (item % 2 == 0)
//                 sumEven += item;
//             else
//                 sumOdd += item;
//         }
//         return sumOdd - sumEven;
//     }
// }
