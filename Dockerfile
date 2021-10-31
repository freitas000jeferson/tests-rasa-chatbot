FROM ubuntu:18.04
ENTRYPOINT []
# CMD []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa --use-feature=2020-resolver
ADD . /app/
RUN chmod +x /app/start_service.sh
CMD /app/start_service.sh
