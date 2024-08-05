import os, sys, time, random, json

with open(f'jsonFiles/capitals.json', 'r') as file:
    topicDict = json.load(file)  
questionKeys = list(topicDict.keys())
random.shuffle(questionKeys)


for question in range(int(5)):
    correctAnswer = topicDict[questionKeys[question]]
    wrongAnswer = list(set(topicDict.values()))

    answerOptions = ( wrongAnswer + [correctAnswer])

#question = (str(self.questions+1) + '. ' +f'{self.questionPhrase} '.capitalize()+ str(questionKeys[question])+ "?\n")

        # formulate the options
    for k in range(len(answerOptions)):
        print(f'{answerOptions[k]}')

