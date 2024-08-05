import os, sys, time, random, json

class QuizLive:
    def __init__(self, topic, questions, Questionphrase):
        self.topic = topic
        self.questions = questions
        self.questionPhrase = Questionphrase
        


        
    
    def createQuizLive(self):
        time.sleep(1)
        print(f'Start:  Quiz {self.topic.title()}.')
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
            print()
            query = f'{question+1}. {self.questionPhrase.capitalize()} {questionKeys[question]}?'
            print(query)

        # formulate the options
            for k in range(len(answerOptions)):
                print(f' {chr(65+k)}. {str(answerOptions[k])}', end='  ')
            print()

        




def getQuizLive():
    answer = input('Make a quiz (y/n): ').lower()
    if answer == 'y':
        topic = input('Choose a topic:')
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






