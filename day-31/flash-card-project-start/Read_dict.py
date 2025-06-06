import pandas
import random

############USING PANDAS READ CSV############
new_word_file = pandas.read_csv("../flash-card-project-start/data/french_words.csv")
# print(new_word_file)
############CONVERT TO DICT(1)############
word_dict = {row.French:row.English for (index, row) in new_word_file.iterrows()}
print(word_dict)
############CONVERT TO DICT(2)############
new_word_dict = {
    "French" : list(word_dict.keys()),
"English" : list(word_dict.values())
}
# print(new_word_dict)
############CONVERT TO DICT(3)############
new_word_dict_1 = new_word_file.to_dict(orient="records")
print(new_word_dict_1) #Same as new_word_dict
############################################
random_card = random.randint(0, 102)
print(random_card)
french_word = new_word_dict["French"][random_card]
english_word = new_word_dict["English"][random_card]
# print(f"{french_word}/{english_word}")

####################################################
new_word_file = pandas.read_csv("../flash-card-project-start/data/french_words.csv")
new_word_dict = new_word_file.to_dict(orient="records")
print(new_word_dict)
