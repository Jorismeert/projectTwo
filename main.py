import os, sys, time, random, json, glob

# correct anwser when incorrect


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
                answer = input(f"\n   Answer: ").strip().upper()  
                if answer in validOptions:
                    userInput = answerList[answer.upper()]
                    # check answer
                    if userInput.lower() == str(correctAnswer).lower():
                        print(f'   {userInput} is correct!', end=' ')
                        self.score += 1
                        self.attempt += 1
                        time.sleep(0.2)
                        break
                    else:
                        print(f'   Incorrect! Correct => {correctAnswer}.', end=' ')
                        self.attempt += 1
                        time.sleep(0.2)
                        break
                else:
                    print(f"Invalid input. Please enter one of the following: {', '.join(validOptions)}")
                    continue
            time.sleep(0.4)
            print(f'        score: {self.score}/{self.attempt}\n')
            time.sleep(1)


def getTopics(directory = "jsonFiles"):
    # Ensure the directory path is correctly formatted
    directory = os.path.abspath(directory)
    # Use glob to find all .json files in the directory
    json_files = glob.glob(os.path.join(directory, '*.json'))
    # Extract the file names from the full paths
    json_filenames = [os.path.basename(file) for file in json_files]
    topics = {}
    for index, element in enumerate(json_filenames):
        element = element.replace('.json',"")
        topics[f'{chr(65+index)}'] = element
    return topics
            

def getQuizLive():
    answer = input('New quiz (y/n): ').lower()
    
    if answer == 'y':
        # prompt the user for a topic
        print('\n Topics: ')      
        topics = getTopics()
        for bulletpoint, topicName in topics.items():
                print(f'{bulletpoint} => {topicName}')
        print('(q to quit)')
        # check userinput for topic
        while True:        
            userInput = input('Choose a topic: ').upper()
            if userInput == 'Q':
                sys.exit()
            elif userInput in topics.keys():
                topic = topics[userInput]
                break
            else:
                print('Not a valid choice!')
                continue
        # prompt user for number questions
        try:
            questions = int(input('How many questions: '))
        except ValueError:
            print('Please enter a number')
        # create a questionPhrase  
        questionsPhrase = input('Creata a question: ')
        return(QuizLive(topic, questions, questionsPhrase))
    else:
        sys.exit()


def main():
    quiz = getQuizLive()
    quiz.createQuizLive()

if __name__=="__main__":
    main()



