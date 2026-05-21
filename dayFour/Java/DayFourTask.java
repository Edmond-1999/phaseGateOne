import java.util.Arrays;

public class DayFourTask{
    public static int[] sumOfTwoNumbers(int[] array, int number){
        int[] newArray = new int[2];
        int count = 0;

        for(int index = 0; index < array.length; index++){
            for(count = 0; count < array.length; count++){
                if(array[index] + array[count] == number){
                    newArray[0] = array[index];
                    newArray[1] = array[count];
                }
            }
            if(newArray[0] == array[index] && newArray[1] == array[count]){
                break;
            }
        }
        return newArray;
    }

    public static int[] rangeBetweenLargestAndSmallestNumbers(int[] array){
        int largest = array[0];

        for(int index = 1; index < array.length; index++){
            if(array[index] > largest){
                largest = array[index];
            }
        }
        int smallest = array[0];

        for(int index = 1; index < array.length; index++){
            if(array[index] < smallest){
                smallest = array[index];
            }
        }

        int[] range = new int[(largest - smallest) + 1];

        for(int index = 0; index < range.length; index++){
            range[index] = smallest;
            smallest++;
        }

        return range;
    }

//    public static String[] consonantOrVowelsInWords(String[] array){
//
//
//    }

    public static void main(String[] args){
        int[] taskOne = {8, 6, 12, 4, -2};
//        System.out.println(Arrays.toString(sumOfTwoNumbers(taskOne, 6)));

        int[] taskThree = {14, 9, 6, 5, 8, 10};

        System.out.println(Arrays.toString(rangeBetweenLargestAndSmallestNumbers(taskThree)));
    }
}
