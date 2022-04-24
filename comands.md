### install

pip3 install -U pip
pip3 install rasa

### create project rasa

python -m venv ./venv
.\venv\Scripts\activate
pip install rasa
rasa init
rasa train
rasa shell
rasa x

#### roda servidor de actions

rasa run actions

#### valida se todos os campos estão corretos

rasa data validate

#### faz uma espécie de debug do rasa

rasa interactive

#### salvar na heroku

> heroku login
> heroku container:login
> heroku container:push web --app=chatbot-rasa-app-test-actions
> heroku container:release web --app=chatbot-rasa-app-test-actions
> heroku logs --tail --app=chatbot-rasa-app-test-service

<!-- chatbot-rasa-app-test-actions -->
<!-- chatbot-rasa-app-test-service -->
