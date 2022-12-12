import requests


#initialize global variables
QUESTION_NUMBER_AMOUNT = 10
QUESTION_TYPE_RESPONSE = 'boolean'
PARAMETERS = {
    'amount': QUESTION_NUMBER_AMOUNT,
    'type': QUESTION_TYPE_RESPONSE,
}
#obtain questions for quiz
RESPONSE = requests.get(url='https://opentdb.com/api.php', params=PARAMETERS)


#check specific response codes
if RESPONSE.status_code == 404:
    raise Exception('That resource does not exist.')
elif RESPONSE.status_code == 401:
    raise Exception('You are not authorized.')


#parsed data from opentdb api results placed into relevant variables
DATA = RESPONSE.json()
QUESTION_DATA = DATA['results']