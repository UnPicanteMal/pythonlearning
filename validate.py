import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|net|guv|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")