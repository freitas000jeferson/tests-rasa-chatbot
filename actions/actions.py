# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime as dt
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

        return []

questions = [{
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
    "q":"I ???? Brazilian and I live in Curitiba.",
    "a": "am",
    "op": [
            {"payload": '/response_to_be{"responses_questions_to_be": "am"}', "title": "am"},
            {"payload":'/response_to_be{"responses_questions_to_be": "is"}', "title": "is"},
            {"payload": '/response_to_be{"responses_questions_to_be": "are"}', "title": "are"}
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

class ActionSendNewQuestionToBe(Action):

    def name(self) -> Text:
        return "action_new_questions_to_be"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = 0
        dispatcher.utter_message(
            text=f"{questionsToBe[id]['q']}",
            buttons=questionsToBe[id]['op'])
        return []

class ActionReciveAnswerToBe(Action):

    def name(self) -> Text:
        return "action_receive_answer_to_be"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = 0
        select = tracker.get_slot("responses_questions_to_be")
        if questionsToBe[id]['a'] == select:
            dispatcher.utter_message(text=f"Esta correto!")
        else: 
            dispatcher.utter_message(text=f"Errou!\nO correto é: {questionsToBe[id]['a']}")
        # dispatcher.utter_message(text=f"voce selecionou: {select}")
        return []