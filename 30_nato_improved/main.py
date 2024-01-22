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

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_csv = "E:/Programming/Python/daily_python/26_nato_alph/nato_phonetic_alphabet.csv"
nato_data = pandas.read_csv(nato_csv)

nato_dict = {}

for (index, row) in nato_data.iterrows():
    nato_dict[row.letter] = row.code

print(nato_dict)

# user_input = list(input(f"Please write your name: ").upper())

# Wouldn't work because it appears alphabetically - Dima -> ['Alfa', 'Delta', 'India', 'Mike']
# necessary_words = [value for (key, value) in nato_dict.items() if key in user_input]

def nato_name():
    try:
        user_input = input(f"Please write your name: ").upper()
        print(user_input)
        result = [nato_dict[letter] for letter in user_input]
        print(result)
    except KeyError:
        print("Only letters from the English alphabet are valid.")
        nato_name()

nato_name()




        
