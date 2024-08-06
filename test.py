import os, sys, time, random, json

class QuizLive:
    def __init__(self, topic, questions, Questionphrase, score=0, attempt=0):
        self.topic = topic
        self.questions = questions
        self.questionPhrase = Questionphrase
        self.score =score
        self.attempt = attempt
    
    def createQuizLive(self):
        time.sleep(1)
        os.system('clear')
        print(f'Start:  Quiz {self.topic.title()}.')
        print()
        time.sleep(2)
        # import json dictionary
        with open(f'jsonFiles/{self.topic}.json', 'r') as file:
            topicDict = json.load(file)  
            
        # create questions
        questionKeys = list(topicDict.keys())
        random.shuffle(questionKeys)
        
        # create random options
        for question in range(int(self.questions)):
            correctAnswer = topicDict[questionKeys[question]]
            wrongAnswer = list(set(topicDict.values()))
            del wrongAnswer[wrongAnswer.index(correctAnswer)]
            wrongAnswer = random.sample(wrongAnswer,3)
            answerOptions = wrongAnswer + [correctAnswer]
            random.shuffle(answerOptions)
        # formulate the question
            query = f'{question+1}. {self.questionPhrase.capitalize()} {questionKeys[question]}?'
            print(query)

        # formulate the options
            answerList = {}
            validOptions = []
            for k in range(len(answerOptions)):
                answerList[f'{chr(65+k)}']=str(answerOptions[k])
            for bulletPoint, answers in answerList.items():
                validOptions.append(bulletPoint)
                print(f'   {bulletPoint}. {answers}')
        # prompt answer + keep track of score
            while True:
                answer = input("\n   Answer: ").strip().upper()  
                if answer in validOptions:
                    userInput = answerList[answer.upper()]
                    # check answer
                    if userInput.lower() == correctAnswer.lower():
                        print('   Correct!')
                        self.score += 1
                        self.attempt += 1
                        time.sleep(0.4)
                        break
                    else:
                        print('   Incorrect!')
                        self.attempt += 1
                        time.sleep(1)
                        break
                else:
                    print(f"Invalid input. Please enter one of the following: {', '.join(validOptions)}")
                    break
            time.sleep(0.4)
            print(f'        score: {self.score}/{self.attempt}\n')
            time.sleep(1)
            

def getQuizLive():
    answer = input('New quiz (y/n): ').lower()
    if answer == 'y':
        topic = input('Choose a topic: ')
        questions = input('How many questions: ')
        questionsPhrase = input('Creata a question: ')
        return(QuizLive(topic, questions, questionsPhrase))
    else:
        sys.exit()


def main():
    quiz = getQuizLive()
    quiz.createQuizLive()

if __name__=="__main__":
    main()

