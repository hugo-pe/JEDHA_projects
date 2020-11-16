print(":::::::::::::: This is a QUIZ GAME ::::::::::::::\n")

######### Defining questions #########

dic_1 = {'question_n1': 'What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton? ', 'a.': '1900', 'b.': '1941', 'c.': '1925', 'd.': '1912', 'correct_answer_1': '1912'}
dic_2 = {'question_n2': 'What is the capital of Portugal? ', 'a.': 'Lisbon', 'b.': 'Madrid', 'c.': 'Rome', 'd.': 'London', 'correct_answer_2': 'Lisbon'}
dic_3 = {'question_n3': 'How many hearts does an Octopus Have? ', 'a.': '1', 'b.': '3', 'c.': '5', 'd.': '9', 'correct_answer_3': '3'}

######### Defining limits #########
counter = 0

######### Ask for an answer for the first question #########
while counter < 3:

  answer_1 = input(dic_1['question_n1'])
  if answer_1 == dic_1['correct_answer_1']:
    counter = counter
    print("Good job! This is the right answer.")
    break
  else:
    counter += 1
    answer_1 != dic_1['correct_answer_1']
    print("Too bad! That is not the correct answer\n")
    if counter == 3:
      print(":( you lost the game!")

######### Ask for an answer for the second question #########
while counter < 3:
  answer_2 = input(dic_2['question_n2']).title() #the answer given by the user will always start with capital letter to match the correct answer

  if answer_2 == dic_2['correct_answer_2']:
    counter = counter
    print("Good job! This is the right answer.")
    break
  else:
    counter += 1
    answer_1 != dic_1['correct_answer_1']
    print("Too bad! That is not the correct answer\n")
    if counter == 3:
      print(":( you lost the game!")

######### Ask for an answer for the third question #########
while counter < 3:
  answer_3 = input(dic_3['question_n3'])

  if answer_3 == dic_3['correct_answer_3']:
    print("Good job! This is the right answer.")
    break
  else:
    counter += 1
    print("Too bad! That is not the correct answer\n")
    if counter == 3:
      print(":( you lost the game!")
