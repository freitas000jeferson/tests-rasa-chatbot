cd app/
# Start rasa server with nlu model
rasa run --model models --enable-api -p $PORT --cors "*" --debug
# Start rasa actions server
# rasa run actions --cors "*" --debug -p $PORT