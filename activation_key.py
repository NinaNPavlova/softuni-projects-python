activation_key = input()

while True:
    command = input().split(">>>")
    action = command[0]
    if action == "Generate":
        break
    elif action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        action_with_letter = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if action_with_letter == "Lower":
            activation_key = (activation_key[:start_index] + activation_key[
                                                                start_index:end_index].lower() + activation_key[
                                                                                                 end_index:])

        elif action_with_letter == "Upper":
            activation_key = (activation_key[:start_index] + activation_key[
                                                                start_index:end_index].upper() + activation_key[
                                                                                                 end_index:])
        print(activation_key)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")