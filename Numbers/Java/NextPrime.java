public class NextPrime {
  public static void main(String args[]) {

    boolean next = true;
    int num = 1;

    do {

      if(isPrime(num)) {
        System.out.println(num);
        System.out.println("Next prime? [y/n]");
        String answer = System.console().readLine();
        if(answer.compareToIgnoreCase("n") == 0) {
          next = false;
        }
      }
      num++;

    } while(next);
  }

  public static boolean isPrime(int num) {
    for(int i = 2; i < num; i++) {
      if(num % i == 0) {
        return false;
      }
    }
    return true;
  }
}