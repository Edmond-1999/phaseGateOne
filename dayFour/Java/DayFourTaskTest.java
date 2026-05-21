import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class DayFourTaskTest{
    public void testSumOfTwoNumbers(){
        int[] array = {8, 6, 12, 4, -2};
        int[] actual = {8, -2};
        int[] expected = DayFourTask.sumOfTwoNumbers(array, 6);
        assertArrayEquals(actual, expected);
    }

}
