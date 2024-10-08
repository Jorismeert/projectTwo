#!/usr/bin/env python3

import os, sys, time, random, json, glob, datetime
from datetime import datetime
# TODO  keep track of highest scores?

class QuizLive:
    def __init__(self, topic, questions, Questionphrase, score=0, attempt=0):
        self.topic = topic
        self.questions = questions
        self.questionPhrase = Questionphrase
        self.score =score
        self.attempt = attempt
    
    def createQuizLive(self):
        # create Header
        time.sleep(0.5)
        os.system('clear')
        print(f'Quiz {self.topic.title().upper()} - {int(self.questions)} questions.')
        time.sleep(0.5)
        print()
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
                answer = input(f"\n   Answer:   ").strip().upper()  
                if answer in validOptions:
                    userInput = answerList[answer.upper()]
                    # check answer
                    if userInput.lower() == str(correctAnswer).lower():
                        print(f'   {userInput} is correct!', end=' ')
                        self.score += 1
                        self.attempt += 1
                        time.sleep(0.8)
                        break
                    else:
                        print(f'   Incorrect!     {questionKeys[question]} => {correctAnswer}.', end=' ')
                        self.attempt += 1
                        time.sleep(0.8)
                        break
                else:
                    print(f"   Invalid input. Please enter one of the following: {', '.join(validOptions)}")
                    continue
            time.sleep(0.4)
            print(f'        score: {self.score}/{self.attempt}\n')
            time.sleep(1)
        attempsLeft = self.questions-self.attempt
        if attempsLeft == 0:
            print(f'        Final result: {self.score}/{self.attempt} - {round((self.score/self.attempt)*100,2)} %') 

        # store score in json file as dictionary
        filepath = 'score.json'
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
        # If the file doesn't exist, start with an empty dictionary
            data = {}
        # Update the dictionary with the new key/value pairs
        newData = {
            datetime.now().strftime("%y-%m-%d %H:%M:%S"): round(((self.score/self.attempt)*100),2) }     
        data.update(newData)
        # Write the updated dictionary back to the JSON file
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)   
        print(f'        Score stored in score.json.\n') 

    
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

def makeQuestion(topic):
    # link the correct question with topic
    if topic == 'capitals':
        questionsPhrase = 'What is the capital of'
    elif topic == 'countries':
        questionsPhrase = 'In which continent is'
    elif topic == 'zipcodesBelgium':
        questionsPhrase = 'Which city has zipcode'
    elif topic == 'citiesBelgium':
        questionsPhrase = 'What is the zipcode of'
    elif topic == 'chemicalElements':
        questionsPhrase = 'What is the symbol of'
    elif topic == 'famousPaintings':
        questionsPhrase = 'Who painted'      
    else:
        questionsPhrase = input('Creata a question: ')
    return questionsPhrase


def getQuizLive():
    # start quiz (y/n)
    answer = input('New quiz (y/n): ').lower()
    # when start quiz (y/n) = y
    if answer == 'y':
        os.system('clear')

        # prompt possible topics 
        print('Topics: ')      
        topics = getTopics()
        for bulletpoint, topicName in topics.items():
                print(f'{bulletpoint} => {topicName}')
        print(' (q to quit)')

        # prompt user for topic input
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
        while True:        
            questions = input('How many questions: ')
            
            if questions.isnumeric() and int(questions) > 0:
                questions = float(questions)
                break  
            else:
                print('Not a valid choice. Enter a number (not zero)!')
                continue
            
        # create a questionPhrase  
        questionsPhrase = makeQuestion(topic)

        # return arguments in class QuizLive
        return(QuizLive(topic, questions, questionsPhrase))

   # when start quiz (y/n) = n
    else:
        sys.exit()


def main():
    quiz = getQuizLive()
    quiz.createQuizLive()

    
if __name__=="__main__":
    main()



