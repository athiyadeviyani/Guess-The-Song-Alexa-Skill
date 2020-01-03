# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the decorators approach in skill builder.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    """Handler for Skill Launch."""
    # type: (HandlerInput) -> Response
    speech_text = "Welcome to guess the song, what type of game do you wish to play?"

    return handler_input.response_builder.speak(
        speech_text).set_should_end_session(False).response


@sb.request_handler(can_handle_func=is_intent_name("StartSongGameIntent"))
def start_song_game_intent_handler(handler_input):
    """Handler for type of game mode Intent."""
    # type: (HandlerInput) -> Response
    mode = handler_input.request_envelope.request.intent.slots["GameMode"].value
    answerType = handler_input.request_envelope.request.intent.slots["AnswerType"].value
    session_attributes = handler_input.attributes_manager.session_attributes
    session_attributes["SessionMode"] = mode
    session_attributes["SessionAswerType"] = answerType
    return handler_input.response_builder.speak(speech_text).set_should_end_session(
        False).response


    
@sb.request_handler(can_handle_func=is_intent_name("SongGuessIntent"))
def song_guess_intent_handler(handler_input):
    """Hanlder for the guess of the song inent."""
    user_guess = handler_input.request_envelope.request.intent.slots["UserGuess"].value
    guess_song
    

@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    """Handler for Help Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "You can say hello to me!"

    return handler_input.response_builder.speak(speech_text).ask(
        speech_text).set_card(SimpleCard(
            "Hello World", speech_text)).response


@sb.request_handler(
    can_handle_func=lambda handler_input:
        is_intent_name("AMAZON.CancelIntent")(handler_input) or
        is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    """Single handler for Cancel and Stop Intent."""
    # type: (HandlerInput) -> Response
    speech_text = "Goodbye!"

    return handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard("Hello World", speech_text)).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.FallbackIntent"))
def fallback_handler(handler_input):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    # type: (HandlerInput) -> Response
    speech = (
        "The Hello World skill can't help you with that.  "
        "You can say hello!!")
    reprompt = "You can say hello!!"
    handler_input.response_builder.speak(speech).ask(reprompt)
    return handler_input.response_builder.response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    """Handler for Session End."""
    # type: (HandlerInput) -> Response
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    # type: (HandlerInput, Exception) -> Response
    logger.error(exception, exc_info=True)

    speech = "Sorry, there was some problem. Please try again!!"
    handler_input.response_builder.speak(speech).ask(speech)

    return handler_input.response_builder.response
    
#pass this to the session: correct_guesses, user_guess, answerType, number, mode    

def play_song(handler_input):
    speech_text = "Here is the song"
    # play song code

def guess_song(artist, name, user_guess, answerType):
    if answerType == "artist":
        if artist == user_guess:
            speech_text = "You guessed correctly, this song is" + title + "played by" + artist 
            correct_guesses += 1
        else:
            speech_text = "You guessed correctly, this song is" + title + "played by" + artist
    elif answerType == "title":
        if title == user_guess:
            speech_text = "You guessed correctly, this song is" + title + "played by" + artist 
            correct_guesses += 1
        else:
            speech_text="You guessed wrong, this song is" + title + "played by" + artist 
    
    return handler_input.response_builder.speak(speech_text)
            
def elimination_mode(answerType):
    play_song(handler_input)
    
    
def number_of_songs_mode(answerType, number):
    for i in range( 0, 5):
        play_song(handler_input)
        guess_song
    
handler = sb.lambda_handler()
