public class CoinFlip {

  public static void main(String args[]) {

    int heads = 0;
    int tails = 0;

    for(int i = 0; i < Integer.parseInt(args[0]); i++) {
      if((System.nanoTime() / 1000) % 2 == 0) heads++; else tails++;
    }

    System.out.println("heads = " + heads);
    System.out.println("tails = " + tails);
  }
}