# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# from util import urlmongo
import pymongo
import random
import datetime as dt
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

id=0
class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []

questions = [
    {
        "q":"???? you like to drink coffee?",
        "a": "do"
    },
    {
        "q":"???? Gabriel have money?",
        "a": "does"
    },
    {
        "q":"???? Carol study Spanish?",
        "a": "does"
    },
    {
        "q":"???? Emily and Louise live in France?",
        "a": "do"
    },
]
questionsToBe= [
    {
        "id":1,
        "q":"I ....... Brazilian and I live in Curitiba.",
        "a": "am",
        "op": [
                {"payload": '/response{"responses_questions": "am"}', "title": "am"},
                {"payload":'/response{"responses_questions": "is"}', "title": "is"},
                {"payload": '/response{"responses_questions": "are"}', "title": "are"}
            ]
    },
    {
        "id":2,
        "q":"..... you talking to me?",
        "a": "are",
        "op": [
                {"payload": '/response{"responses_questions": "am"}', "title": "am"},
                {"payload":'/response{"responses_questions": "is"}', "title": "is"},
                {"payload": '/response{"responses_questions": "are"}', "title": "are"}
            ]
    },
    {
        "id":3,
        "q":"What ........ Sheila doing?",
        "a": "am",
        "op": [
                {"payload": '/response{"responses_questions": "am"}', "title": "am"},
                {"payload":'/response{"responses_questions": "is"}', "title": "is"},
                {"payload": '/response{"responses_questions": "are"}', "title": "are"}
            ]
    },
    {
        "id":5,
        "q":"My dog ........ playing in the garden.",
        "a": "am",
        "op": [
                {"payload": '/response{"responses_questions": "am"}', "title": "am"},
                {"payload":'/response{"responses_questions": "is"}', "title": "is"},
                {"payload": '/response{"responses_questions": "are"}', "title": "are"}
            ]
    },
    {
        "id":4,
        "q":"My dog ........ playing in the garden.",
        "a": "am",
        "op": [
                {"payload": '/response{"responses_questions": "am"}', "title": "am"},
                {"payload":'/response{"responses_questions": "is"}', "title": "is"},
                {"payload": '/response{"responses_questions": "are"}', "title": "are"}
            ]
    },

]
questionsPrepositions = [
    {
        "id":1,
        "q":"I met him ……………………… Monday.",
        "a": "on",
        "op": [
                {"payload": '/response{"responses_questions": "on"}', "title": "on"},
                {"payload":'/response{"responses_questions": "in"}', "title": "in"},
                {"payload": '/response{"responses_questions": "at"}', "title": "at"}
            ]
    },
    {
        "id":2,
        "q":"They took him ……………………… the doctor.",
        "a": "on",
        "op": [
                {"payload": '/response{"responses_questions": "on"}', "title": "on"},
                {"payload":'/response{"responses_questions": "in"}', "title": "in"},
                {"payload": '/response{"responses_questions": "to"}', "title": "to"}
            ]
    },
    {
        "id":3,
        "q":"Regular exercise is beneficial ……………………… health.",
        "a": "to",
        "op": [
                {"payload": '/response{"responses_questions": "on"}', "title": "on"},
                {"payload":'/response{"responses_questions": "to"}', "title": "to"},
                {"payload": '/response{"responses_questions": "with"}', "title": "with"}
            ]
    },
    {
        "id":4,
        "q":"There are many disadvantages ……………………… living alone.",
        "a": "to",
        "op": [
                {"payload": '/response{"responses_questions": "for"}', "title": "for"},
                {"payload":'/response{"responses_questions": "of"}', "title": "of"},
                {"payload": '/response{"responses_questions": "to"}', "title": "to"}
            ]
    },
    {
        "id":5,
        "q":"The cat jumped ………………………… the wall.",
        "a": "over",
        "op": [
                {"payload": '/response{"responses_questions": "across"}', "title": "across"},
                {"payload":'/response{"responses_questions": "over"}', "title": "over"},
                {"payload": '/response{"responses_questions": "through"}', "title": "through"}
            ]
    },
]

class ActionSendNewQuestion(Action):

    def name(self) -> Text:
        return "action_new_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = 0
        dispatcher.utter_message(text=f"{questions[id]['q']}")
        
        return [SlotSet("ans_id_question", id)]

class ActionReciveAnswer(Action):

    def name(self) -> Text:
        return "action_recive_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ans = tracker.latest_message['text']
        id = tracker.get_slot("ans_id_question")
        print( "ans-> ",ans, "| ", questions[id]['a'] )
        if questions[id]['a'] == ans:
            dispatcher.utter_message(text=f"Yeeeess!!! esta correto")
        else: 
            dispatcher.utter_message(text=f"Não foi dessa vez!!!\no correto é '{questions[id]['a']}'")

        return [SlotSet("ans_question", ans)]

# ##########
class ActionSendNewQuestionToBe(Action):

    def name(self) -> Text:
        return "action_new_questions_to_be"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # id = random.randint(0, 4)
        id=0
        question = connectMongo()
        print(question)
        # dispatcher.utter_message(
        #     text=f"{questionsToBe[id]['q']}",
        #     buttons=questionsToBe[id]['op'])
        dispatcher.utter_message(
            text=f"{question['question']}",
            buttons=question['options'])
        return [SlotSet("ans_id_question", id)]

class ActionReciveAnswerToBe(Action):

    def name(self) -> Text:
        return "action_receive_answer_to_be"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot("ans_id_question")
        select = tracker.get_slot("responses_questions")
        if questionsToBe[id]['a'] == select:
            dispatcher.utter_message(text=f"Esta correto!")
        else: 
            dispatcher.utter_message(text=f"Errou!\nO correto é: {questionsToBe[id]['a']}")
        # dispatcher.utter_message(text=f"voce selecionou: {select}")
        return []
# ------------
class ActionSendNewQuestionPrepositions(Action):

    def name(self) -> Text:
        return "action_new_questions_preposition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = random.randint(0, 4)
        dispatcher.utter_message(
            text=f"{questionsPrepositions[id]['q']}",
            buttons=questionsPrepositions[id]['op'])
        return [SlotSet("ans_id_question", id)]

class ActionReciveAnswerPrepositions(Action):

    def name(self) -> Text:
        return "action_receive_answer_preposition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.get_slot("ans_id_question")
        select = tracker.get_slot("responses_questions")
        if questionsPrepositions[id]['a'] == select:
            dispatcher.utter_message(text=f"Esta correto!")
        else: 
            dispatcher.utter_message(text=f"Errou!\nO correto é: {questionsPrepositions[id]['a']}")
        # dispatcher.utter_message(text=f"voce selecionou: {select}")
        return []

def connectMongo():
    # url = urlmongo()
    myclient = pymongo.MongoClient( 'mongodb+srv://freitas000jeferson:92028867Jef@cluster0.eetke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = myclient["rasa"]
    collection = db["questions"]
    query = { "category": "TO_BE" }

    listdocs = collection.find(query)
    # for x in listdocs:
    #     print(x)
    return listdocs[0]