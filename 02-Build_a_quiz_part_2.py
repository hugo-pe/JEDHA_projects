 def quiz():
      dic = {'What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton? ': '1912', 'What is the capital of Portugal? ': 'Lisbon', 'How many hearts does an Octopus Have?': '3'}

      counter = 0
      for q,a in dic.items():
        while counter < 3:
          quiz_question = print(q)
          quiz_answer = input("Your answer : ")
          if quiz_answer == a:
              print("Good job! This is the right answer.\n")
              break
          else:
              print("Too bad! That is not the correct answer\n")
              counter += 1
              if counter >= 3:
                  print("\n:( you lost the game!")   
