"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and 
for the multiples of five output “Buzz”. For numbers which are multiples of 
both three and five output “FizzBuzz”.

https://leetcode.com/problems/fizz-buzz/
"""
class Solution:
    def fizzBuzz(self, n):
        results =[]
        for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                results.append('FizzBuzz')
            elif (i % 3 == 0):
                results.append('Fizz')
            elif (i % 5 == 0):
                results.append('Buzz')
            else:
                results.append(str(i))
        return results

if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
