class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # go_on = True
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
            # go_on = False
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is : {self.score}/{self.question_number}\n")
        # OR
        #self.final_score = f"{self.score}/{self.question_number}"
        #print(f"Your current score is: {self.final_score}.\n")

        #
        # if not go_on:
        #     exit()
