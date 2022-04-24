import requests

url = 'https://chatbot-rasa-app-test-service.herokuapp.com/webhooks/rest/webhook' 
myobj = {
"message": "ola",
"sender": 1,
}
x = requests.post(url, json = myobj)
print(x.text)