#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Udemy-Angela-Yu/D24_Merge_Mail/Input/Names/invited_names.txt") as names:
    list_names = names.readlines()
    print(list_names)

with open("./Udemy-Angela-Yu/D24_Merge_Mail/Input/Letters/starting_letter.txt") as original_letter:
    original_letter_content = original_letter.read()
    for name in list_names:
        with open(f"./Udemy-Angela-Yu/D24_Merge_Mail/Output/ReadyToSend/{name.strip()}_letter.txt", "w") as modified_letter:
            modified_letter_content = original_letter_content.replace("[name]", name.strip())
            modified_letter.write(modified_letter_content)
