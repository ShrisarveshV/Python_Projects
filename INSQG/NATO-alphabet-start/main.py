import pandas
student_data_frame= pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in student_data_frame.iterrows():
    pass
stud={row.letter:row.code for (index,row) in student_data_frame.iterrows()}
print(stud)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

