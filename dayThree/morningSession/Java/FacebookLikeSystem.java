public class FacebookLikeSystem{
    public static String theLikesOfPeople(String[] array){
        lengthOfArray = array.length;

        if(lengthOfArray == 0){
            return "No one likes this";
        }
        else if(lengthOfArray == 1){
            return array[0] + " likes this";
        }
        else if(lengthOfArray == 2){
            return array[0] + " and " + array[1] " like this";
        }
        else if(lengthOfArray == 3){
            return array[0] + ", " + array[1]" and " + array[2] + " like this"; 
        }
        else{
            return array[0] + ", " + array[1] " and " (lengthOfArray - 2) " like this"; 
        }
    }
}
