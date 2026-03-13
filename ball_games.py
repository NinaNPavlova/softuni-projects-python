from collections import deque

strength = [int(el) for el in input().split()]
accuracy = deque(int(el) for el in input().split())

current_strength = list(strength)
current_accuracy = deque(accuracy)
goals = 0

while current_strength and current_accuracy:
    result = current_strength[-1] + current_accuracy[0]

    if result == 100:
        goals += 1
        current_strength.pop()
        current_accuracy.popleft()

    elif result < 100:
        if current_strength[-1] < current_accuracy[0]:
            current_strength.pop()
        elif current_strength[-1] > current_accuracy[0]:
            current_accuracy.popleft()
        else:
            value = current_strength.pop()
            current_strength.append(value + current_accuracy[0])
            current_accuracy.popleft()

    else:
        value = current_strength.pop()
        current_strength.append(value - 10)
        current_accuracy.rotate(-1)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")
else:
    print("Paul failed to score a single goal.")

if goals > 0:
    print(f"Goals scored: {goals}")

if current_strength:
    print(f"Strength values left: {', '.join(map(str, current_strength))}")
if current_accuracy:
    print(f"Accuracy values left: {', '.join(map(str, current_accuracy))}")