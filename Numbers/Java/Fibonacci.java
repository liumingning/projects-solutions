public class Fibonacci {

  public static void main(String args[]) {
    calcFibonacci(1, 0, 12, 0, true);
  }

  public static int calcFibonacci(int current, int previous, int limit, int elements, boolean limitElements) {
    
    elements++;
    
    if(limitElements && elements > limit) {
      return 0;
    } else if(!limitElements && current > limit) {
      return 0;
    }

    System.out.println("element " + elements + " = " + current);
    return calcFibonacci(current + previous, current, limit, elements, limitElements);
  }
}