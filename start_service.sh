cd app/
# Start rasa server with nlu model
rasa run --model models --enable-api -p $PORT --cors "*" --debug --endpoints heroku-endpoints.yml
