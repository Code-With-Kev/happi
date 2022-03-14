from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB
from enum import Enum

class State(str, Enum):
    QUESTION_1 = "Which direction do you like your toilet paper to face?"
    QUESTION_2 = "The supervisor you hate the most is waving at you like you're bff's. How do you act?"
    QUESTION_2a = "The supervisor you hate the most is waving at you like you're bff's. How do you act?"
    QUESTION_2b = "The supervisor you hate the most is waving at you like you're bff's. How do you act?"
    QUESTION_3 = "Who has the sexier superheroes: Marvel or DC?"
    QUESTION_4 = "You're Batman! Joker is across town wrecking havoc. What do you do?"
    QUESTION_5 = "You're Thor! Loki is across town wrecking havoc. What do you do?"
    QUESTION_6 = "In a videogame, you are most likely to be a:"
    QUESTION_7 = "You're running late to a date you met on Tinder. What saddens you more?"
    QUESTION_8 = "The crypto coin all your friends forced you to invest in just skyrocketed. You're rich! What's the first thing you do?;"
    QUESTION_9 = "You're favorite character on the Netflix show you're watching is about to die. How do you feel?"
    QUESTION_10a = "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?"
    QUESTION_10b = "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?"
    QUESTION_10c = "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?"
    QUESTION_10d = "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?"
    QUESTION_10e = "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?"
    RESULT_1 = "You are hostile and dominant (and cant beat me in Mario Party)"
    RESULT_2 = "You are dominant (and cant beat me in Mario Party)"
    RESULT_3 = "You are warm and dominant (and cant beat me in Mario Party)"
    RESULT_4 = "You are hostile and submissive (and cant beat me in Mario Party)"
    RESULT_5 = "You are submissive (and cant beat me in Mario Party)"
    RESULT_6 = "You are warm and submissive (and cant beat me in Mario Party)"
    
class Trigger(str, Enum):
    ANSWER_1 = "Over"
    ANSWER_2 = "Under"
    ANSWER_3 = "Become superficially friendly and fake affection"
    ANSWER_4 = "Pretend you didn't see them and keep walking"
    ANSWER_5 = "Warrior"
    ANSWER_6 = "Mage"
    ANSWER_7 = "Marvel"
    ANSWER_8 = "DC"
    ANSWER_9 = "Disappointing myself"
    ANSWER_10 = "Disappointing them"
    ANSWER_11 = "SHOPPING!!!"
    ANSWER_12 = 'Time to start saving and investing!'
    ANSWER_13 = 'Plan the best way to get a surprise attack'
    ANSWER_14 = "Screw planning! LET'S GO KICK SOME A-"
    ANSWER_15 = 'Plan the best way to get a surprise attack'
    ANSWER_16 = "Screw planning! LET'S GO KICK SOME A-"
    ANSWER_17 = "It's not that deep"
    ANSWER_18 = 'Become anxious and depressed'
    ANSWER_19a = 'Gloat all up in their face'
    ANSWER_20a = 'Accept my win graciously'
    ANSWER_19b = 'Gloat all up in their face'
    ANSWER_20b = 'Accept my win graciously'
    ANSWER_19c = 'Gloat all up in their face'
    ANSWER_20c = 'Accept my win graciously'
    ANSWER_19d = 'Gloat all up in their face'
    ANSWER_20d = 'Accept my win graciously'
    ANSWER_19e = 'Gloat all up in their face'
    ANSWER_20e = 'Accept my win graciously'

rules = {
    State.QUESTION_1 : [
        (Trigger.ANSWER_1, State.QUESTION_2a),
        (Trigger.ANSWER_2, State.QUESTION_2b),
    ],
    State.QUESTION_2a: [
        (Trigger.ANSWER_3, State.QUESTION_6),
        (Trigger.ANSWER_4, State.QUESTION_3),
    ],
    State.QUESTION_2b : [
        (Trigger.ANSWER_3, State.QUESTION_3),
        (Trigger.ANSWER_4, State.QUESTION_7),
    ],
    State.QUESTION_3: [
        (Trigger.ANSWER_7, State.QUESTION_5),
        (Trigger.ANSWER_8, State.QUESTION_4),
    ],
    State.QUESTION_4 : [
        (Trigger.ANSWER_15, State.QUESTION_10c),
        (Trigger.ANSWER_16, State.QUESTION_10d),
    ],
    State.QUESTION_5 : [
        (Trigger.ANSWER_13 , State.QUESTION_10b),
        (Trigger.ANSWER_14, State.QUESTION_10c),
    ],
    State.QUESTION_6: [
        (Trigger.ANSWER_5, State.QUESTION_8),
        (Trigger.ANSWER_6, State.QUESTION_5),
    ],
    State.QUESTION_7 : [
        (Trigger.ANSWER_9, State.QUESTION_4),
        (Trigger.ANSWER_10, State.QUESTION_9),
    ],
    State.QUESTION_8 : [
        (Trigger.ANSWER_11, State.QUESTION_10a),
        (Trigger.ANSWER_12, State.QUESTION_10b),
    ],
    State.QUESTION_9 : [
        (Trigger.ANSWER_17, State.QUESTION_10d),
        (Trigger.ANSWER_18, State.QUESTION_10e),
    ],
    State.QUESTION_10a : [
        (Trigger.ANSWER_19a, State.RESULT_1),
        (Trigger.ANSWER_20a, State.RESULT_2),
    ],
    State.QUESTION_10b : [
        (Trigger.ANSWER_19b, State.RESULT_2),
        (Trigger.ANSWER_20b, State.RESULT_3),
    ],
    State.QUESTION_10c : [
        (Trigger.ANSWER_19c, State.RESULT_3),
        (Trigger.ANSWER_20c, State.RESULT_4),
    ],
    State.QUESTION_10d : [
        (Trigger.ANSWER_19d, State.RESULT_4),
        (Trigger.ANSWER_20d, State.RESULT_5),
    ],
    State.QUESTION_10e : [
        (Trigger.ANSWER_19e, State.RESULT_5),
        (Trigger.ANSWER_20e, State.RESULT_6),
    ],
}