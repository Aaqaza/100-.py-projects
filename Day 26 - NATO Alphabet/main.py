#  Keyword Method with iterrows()
#  {new_key:new_value for (index, row) in df.iterrows()}

import pandas
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1: Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}

word = input("Enter your word: ").upper()

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.
nato_alphabets = [phonetic_dict[letter] for letter in word]
print(nato_alphabets)





# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
