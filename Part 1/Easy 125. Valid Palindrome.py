import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        letters = re.sub(r"[^A-Za-z0-9]", "", s)
        letters = letters.lower()
        length = len(letters)

        # Check if the string is empty or consists of a single character (palindrome by definition)
        if length <= 1:
            return True

        # Define left and right ranges based on string length (odd or even)
        if length % 2 == 0:
            left_range = range(length // 2 - 1, -1, -1)
            right_range = range(length // 2, length)
        else:
            left_range = range(length // 2 - 1, -1, -1)
            right_range = range(length // 2 + 1, length)

        # Compare characters at corresponding positions in the ranges
        for left, right in zip(left_range, right_range):
            if letters[right] != letters[left]:
                return False

        return True


# Test cases
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False
print(solution.isPalindrome("abcba"))  # True
print(solution.isPalindrome("12321"))  # True
print(solution.isPalindrome("Able was I, ere I saw Elba"))  # True
print(solution.isPalindrome("Palindrome"))  # False
