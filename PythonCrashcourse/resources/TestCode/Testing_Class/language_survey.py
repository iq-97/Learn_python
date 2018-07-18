from survey import AnonymousSurvey

#define a question, and make a survey
question = "Que primer lenguaje aprendiste para hablar"
my_survey = AnonymousSurvey(question)


# Show the question, and store responses to the question

my_survey.show_question()
print("Enter 'q' at any time to quite. \n")
while True:
    response = input("Lenguaje: ")
    if response == 'q':
        break
    my_survey.store_response(response)

#show the survey results/
print("\n Thank you to everyone who participated in the survey! ")
my_survey.show_results()