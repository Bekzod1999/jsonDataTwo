import requests
import json

allResults = []
dictionary1 = {}
url = 'https://randomuser.me/api'

for i in range(20):
    response = requests.get(url)
    jsonFile = response.json()
    allResults.append(jsonFile)

dictionary1['result'] = allResults
jsonObject = json.dumps(dictionary1)
file = open('data.json', 'w')
file.write(jsonObject)

json_data = open("data.json", 'r', encoding='utf-8')
dictionaryData = json.load(json_data)

getDictionaryDataResult = dictionaryData['result']
lengthResultList = len(getDictionaryDataResult)

allNewResultsForMale = []
allNewResultsForFemale = []

for i in range(lengthResultList):
    newInformationForMale = {}
    newInformationForFemale = {}

    easy = getDictionaryDataResult[i]['results'][0]
    easyFAndL = getDictionaryDataResult[i]['results'][0]['name']

    if easy['gender'] == 'male':
        newInformationForMale['gender'] = 'male'
        newInformationForMale['firstName'] = easyFAndL['first']
        newInformationForMale['lastName'] = easyFAndL['last']
        newInformationForMale['age'] = easy['dob']['age']
        newInformationForMale['country'] = easy['location']['country']
        allNewResultsForMale.append(newInformationForMale)
    else:
        newInformationForFemale['gender'] = 'female'
        newInformationForFemale['firstName'] = easyFAndL['first']
        newInformationForFemale['lasttName'] = easyFAndL['last']
        newInformationForFemale['age'] = easy['dob']['age']
        newInformationForFemale['country'] = easy['location']['country']
        allNewResultsForFemale.append(newInformationForFemale)

# for male
allNewDictionaryForMale = {}
allNewDictionaryForMale['result'] = allNewResultsForMale
maleJsonObject = json.dumps(allNewDictionaryForMale)
writeJsonForMale = open('male.json', 'w')
writeJsonForMale.write(maleJsonObject)
# for Female
allNewDictionaryForFemale = {}
allNewDictionaryForFemale['result'] = allNewResultsForFemale
femaleJsonObject = json.dumps(allNewDictionaryForFemale)
writeJsonForFemale = open('female.json', 'w')
writeJsonForFemale.write(femaleJsonObject)