# CachingAlgorithm
A very specific caching algorithm for calculating prime numbers
I needed to create Python code which is able to take in a binary string of any length, followed by a given value (N) such as 123. This python code then must, according to the project specification, generate every possible substring from this binary string. 
For example, “10101” - this string can be split into: 
1 
10 
101 
so on, and so forth, as well as segmented in the middle, for example: 
10(101)110 
These substrings are converted to their decimal equivalent (base 10), so the binary string 101 becomes 5. 
These substrings are then checked if they are prime numbers or not, if they are, then: 
All prime substrings and their decimal values are compared to the 2nd input (the given value after the binary string, N) to see if they are more (or less) in value. If they are more: then they are not used in the output, as this 2nd given value is used to determine the biggest prime number output within the algorithm.
So, for example, if the 2nd given value (N), is 123 then we will not output the substring resulting in the value 16787, as it is a prime number, however; its more than value of N (123) 

If there are more than 6 prime numbers found, then the output of the program will be the first 3 and last 3 primes 
(smallest to biggest) 
If there are less than 6 prime numbers found, then the output of the program will simply output all of the primes. 
The program also outputs the exact number of primes found, so for example an expected output could be: 

9: 2, 3, 5, 17, 19, 23 

this is broken down as: 

9: <- the amount of prime numbers 

2, 3, 5 <- the first 3 prime numbers 

17, 19, 23 <- the last 3 prime numbers
