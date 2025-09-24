
#reading in the names from invited_names.txt into the names variable
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    #striping out the return characters
    for name in names:
        names[names.index(name)] = name.strip("\n")

#reading in the lines from starting_letter.txt into the letter variable
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

#Replace the [name] placeholder with the actual name.
for name in names:
    new_letter = []
    for line in letter:
        new_letter.append(line.replace("[name]", name))
    #write the new letter to a file in the "ReadyToSend" folder
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.writelines(new_letter)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp