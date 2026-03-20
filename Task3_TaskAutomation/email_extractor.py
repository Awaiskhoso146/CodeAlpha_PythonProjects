# Email Extactor Python Project

import re

with open("data.txt", "r") as file:
    text = file.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")
        print("Extracted email:", email)

print("Email extracted successfully")
