import java.util.*;

public class OptimizedPrimeSieve {

    public static List<Integer> sieveOptimized(int n) {
        List<Integer> primes = new ArrayList<>();
        if (n < 2) return primes;

        // 2 is the only even prime
        primes.add(2);

        // Only track odd numbers
        boolean[] isPrime = new boolean[(n - 1) / 2];
        Arrays.fill(isPrime, true);

        for (int i = 3; i * i <= n; i += 2) {
            if (isPrime[(i - 3) / 2]) {
                for (int j = i * i; j <= n; j += 2 * i) {
                    isPrime[(j - 3) / 2] = false;
                }
            }
        }

        for (int i = 3; i <= n; i += 2) {
            if (isPrime[(i - 3) / 2]) {
                primes.add(i);
            }
        }

        return primes;
    }

    public static void main(String[] args) {
        int n = 35;
        System.out.println(sieveOptimized(n));
    }
}

