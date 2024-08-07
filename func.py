import os, sys, time, random, json, glob

def getTopics(directory="jsonFiles"):
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
    if topic == 'capitals':
        questionsPhrase = 'What is the capital of'
    elif topic == 'countries':
        questionsPhrase = 'In which continent is'
    elif topic == 'zipcodesBelgium':
        questionsPhrase = 'Which city has zipcode'
    elif topic == 'citiesBelgium':
        questionsPhrase = 'What is the zipcode of'
    else:
        questionsPhrase = input('Creata a question: ')
    return questionsPhrase
        
    

def main():

    topics = getTopics()
    for bulletpoint, topicName in topics.items():
            print(f'{bulletpoint} => {topicName}')
    print('(q to quit)')
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
    print(topic)

if __name__== "__main__":
    main()