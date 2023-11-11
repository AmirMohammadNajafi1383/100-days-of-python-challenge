student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import csv
nato_phonetic_alphabet = {}
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open('nato_phonetic_alphabet.csv','r')as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        letter = row['letter']
        code = row['code']
        nato_phonetic_alphabet[letter] = code
print(nato_phonetic_alphabet)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input('Enter a word:').upper()

phonetic_word = [nato_phonetic_alphabet[letter] for letter in input_word if letter in nato_phonetic_alphabet]
 
print(phonetic_word)