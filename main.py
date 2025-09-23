#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

#strip out the return characters
for name in names:
    names[names.index(name)] = name.strip("\n")

print(names)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp