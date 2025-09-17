from collections import deque


substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
secondary_requirements = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

found_colors = []

while substrings:

    if len(substrings) == 1:
        first = substrings.popleft()
        last = ""
    else:
        first = substrings.popleft()
        last = substrings.pop()


    combo1 = first + last
    combo2 = last + first

    color = ""
    if combo1 in main_colors | secondary_colors:
        color = combo1
    elif combo2 in main_colors | secondary_colors:
        color = combo2

    if color:
        found_colors.append(color)
    else:

        first, last = first[:-1], last[:-1]
        mid = len(substrings) // 2
        if last:
            substrings.insert(mid, last)
        if first:
            substrings.insert(mid, first)

final_colors = []
for color in found_colors:
    if color in secondary_colors:
        if secondary_requirements[color].issubset(final_colors):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)
