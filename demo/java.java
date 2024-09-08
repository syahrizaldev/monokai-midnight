// 1. Example
public class ReverseNumber {

   public static void main(String[] args) {
      int number = 1234;
      int reversedNumber = 0;
      int temp = 0;

      while(number > 0){
         temp = number%10;
         reversedNumber = reversedNumber * 10 + temp;
         number = number/10;
      }

      System.out.println("Reversed Number is: " + reversedNumber);
   }
}

// 2. Tests
public class Test {
   public void test(Object a) {
      System.out.println("hello");
      if(a instanceof String) {
         System.out.println("it's me");
      }
   }
}
