import requests

def plag_check(text_to_check):
    api_key = 'API_KEY'
    url = f'https://api.prepostseo.com/apis/checkPlag?key={api_key}&data={text_to_check}'

    response = requests.get(url)
    result = response.json()
    print(result)

    # if result['percentage'] > 0:
    #     print(f"Plagiarism detected: {result['percentage']}%")
    #     print(f"Sources: {result['sources']}")
    # else:
    #     print("No plagiarism detected.")