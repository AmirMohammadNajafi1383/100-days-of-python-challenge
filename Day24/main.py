#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
     #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp 
PLACEHOLDER ='[name]'
with open('Input/Names/invited_names.txt', mode='r') as f:
    names_file = f.readlines()

    

with open('Input/Letters/starting_letter.txt', mode='r') as file:  # Use a different variable name here
    file_txt = file.read()  # Use 'file' instead of 'f' to read from the second file
    for name in names_file:
        stripped_name = name.strip()
        new_letter=file_txt.replace(PLACEHOLDER,stripped_name)
        with open(f'./Output/ReadyToSend/example.txt',mode='w') as f:
            letter_complate = f.write(new_letter)
            print(letter_complate)  


