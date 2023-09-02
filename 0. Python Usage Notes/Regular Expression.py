import re

# Common Regular Expression Patterns with Detailed Comments:
# --------------------------------------------------------

# 1. Matching Digits (\d):
#    - \d matches any single digit (0-9).
pattern = r"\d"

# 2. Matching Word Characters (\w):
#    - \w matches any word character, which includes letters, digits, and underscore.
pattern = r"\w"

# 3. Matching White Space (\s):
#    - \s matches any whitespace character, including spaces, tabs, and newlines.
pattern = r"\s"

# 4. Matching Email Addresses (Basic):
#    - [a-zA-Z0-9._%+-]+ matches the username part of the email address.
#    - @[a-zA-Z0-9.-]+ matches the @ symbol and the domain name.
#    - \.[a-zA-Z]{2,} matches the top-level domain (TLD) with at least two characters.
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# 5. Matching URLs (Basic):
#    - (https?|ftp):// matches either "http", "https", or "ftp".
#    - [^\s/$.?#].[^\s]* matches the domain part of the URL.
pattern = r"(https?|ftp)://[^\s/$.?#].[^\s]*"

# 6. Matching Dates (MM/DD/YYYY format):
#    - ^ matches the start of the string.
#    - (0[1-9]|1[0-2]) matches the month in MM format (01-12).
#    - / matches the separator between month and day.
#    - (0[1-9]|[12][0-9]|3[01]) matches the day in DD format (01-31).
#    - / matches the separator between day and year.
#    - \d{4} matches the year in YYYY format (e.g., 2023).
#    - $ matches the end of the string.
pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"

# 7. Matching Phone Numbers (U.S.):
#    - \d{3}-\d{3}-\d{4} matches the format XXX-XXX-XXXX for U.S. phone numbers.
pattern = r"\d{3}-\d{3}-\d{4}"

# 8. Matching HTML Tags (Basic):
#    - <[^>]+> matches any HTML tag, including its attributes.
pattern = r"<[^>]+>"

# 9. Matching IPv4 Addresses:
#    - (\d{1,3}\.){3} matches the first three parts of the IPv4 address (e.g., 192.168.1.).
#    - \d{1,3} matches the last part of the IPv4 address (e.g., 1).
pattern = r"(\d{1,3}\.){3}\d{1,3}"

# 10. Matching Zip Codes (U.S.):
#     - \d{5} matches the five-digit ZIP code.
#     - (-\d{4})? makes the last four digits optional (ZIP+4 format).
pattern = r"\d{5}(-\d{4})?"

# Note: These comments provide an explanation of what each regular expression does. You can modify and use them based on your specific text processing needs.
