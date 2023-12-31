class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        i = 0
        n = len(s)
        result = 0
        is_negative = False

        # Step 1: Skip leading whitespaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check if the next character is '-' or '+'
        if i < n and (s[i] == "-" or s[i] == "+"):
            is_negative = s[i] == "-"
            i += 1

        # Step 3: Read in the next characters until a non-digit character
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow and underflow
            if (result > INT_MAX // 10) or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MIN if is_negative else INT_MAX
            result = result * 10 + digit
            i += 1

        return -result if is_negative else result


# Test cases
sol = Solution()
print(sol.myAtoi("42"))  # Expected output: 42
print(sol.myAtoi("   -42"))  # Expected output: -42
print(sol.myAtoi("4193 with words"))  # Expected output: 4193
print(
    sol.myAtoi("words and 987")
)  # Expected output: 0 (since it starts with non-whitespace characters that are non-digits)
print(sol.myAtoi("-91283472332"))  # Expected output: -2147483648 (clamped to INT_MIN)
print(sol.myAtoi("+-2"))  # Expected output: 0
