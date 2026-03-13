import re

text = input()
numbers = []
cool_threshold = 1
for n in text:
    if n.isdigit():
        cool_threshold *= int(n)

current_cool_threshold = 0
all_emoji = []
cool_emoji = []

pattern = r"(\*\*|::)([A-Z]{1}[a-z]{2,})\1"
matches = re.finditer(pattern, text)
for match in matches:
    full_emoji = match.group(1) + match.group(2) + match.group(1)
    emoji = match.group(2)
    all_emoji.append(full_emoji)
    current_threshold = sum(ord(char) for char in match.group(2))
    if current_threshold >= cool_threshold:
        cool_emoji.append(full_emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emoji)} emojis found in the text. The cool ones are: ")
print("\n".join(cool_emoji))
