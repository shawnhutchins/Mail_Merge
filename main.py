PLACEHOLDER = "[name]"

#reading in the names from invited_names.txt into the names variable
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    #striping out the return characters
    for name in names:
        names[names.index(name)] = name.strip("\n")

#reading in the lines from starting_letter.txt into the letter variable
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

#Replace the [name] placeholder with the actual name.
for name in names:
    new_letter = letter.replace(PLACEHOLDER, name)
    #write the new letter to a file in the "ReadyToSend" folder
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
