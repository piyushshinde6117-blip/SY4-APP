import re

# 1. Define the sample text to search through
sample_text = "Call us at support@example.com or reach sales@company.org!"

# 2. Define the regex pattern for emails
# [a-zA-Z0-9._%+-]+ -> Username (letters, numbers, dots, plus, etc.)
# @                 -> The '@' symbol
# [a-zA-Z0-9.-]+    -> Domain name (e.g., 'example' or 'company')
# \.[a-zA-Z]{2,}    -> Dot followed by domain extension (e.g., '.com', '.org')
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# 3. Find all matches in the text
emails = re.findall(email_pattern, sample_text)

# 4. Print the results
print("Found emails:")
for email in emails:
    print(email)