echo PORT $PORT
# rasa run -p $PORT --cors "*" --debug --endpoints heroku-endpoints.yml
rasa run actions -p $PORT --cors "*" --debug