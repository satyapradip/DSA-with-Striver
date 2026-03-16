import java.util.*;

public class SieveOfEratosthenes {

    public static List<Integer> findPrimes(int n) {
        // 1. Create a boolean array. 
        // Index 'i' represents the number 'i'.
        // Default value of boolean is false, so we fill it with true initially.
        boolean[] isPrime = new boolean[n + 1]; // n+1 because we want to include the number n itself
        Arrays.fill(isPrime, true); // fill the array with true initially

        // 0 and 1 are not prime numbers
        if (n >= 0) isPrime[0] = false; // 0 is not a prime number  
        if (n >= 1) isPrime[1] = false; // 1 is not a prime number

        // 2. The Sieve Logic
        // We only need to run the outer loop up to the square root of n
        for (int p = 2; p * p <= n; p++) {
            
            // If isPrime[p] is still true, then p is a prime
            if (isPrime[p]) {
                
                // Update all multiples of p to false (not prime)
                // Optimization: Start at p * p. 
                // Any multiple less than p * p has already been marked by a smaller prime.
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        // 3. Collect the primes into a list
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }
        
        return primes;
    }

    public static void main(String[] args) {
        int n = 50;
        List<Integer> result = findPrimes(n);
        
        System.out.println("Primes less than or equal to " + n + ":");
        System.out.println(result);
    }
}