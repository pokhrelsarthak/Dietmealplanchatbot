"""
 This code sample demonstrates an implementation of the Lex Code Hook Interface
 in order to serve a bot which manages banking account services. Bot, Intent, 
 and Slot models which are compatible with this sample can be found in the Lex 
 Console as part of the 'AccountServices' template.
"""
import json
import time
import os
import logging
import dialogstate_utils as dialog
import weight_loss_intent
import weight_gain_intent

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
    
# --- Main handler & Dispatch ---

def dispatch(intent_request):
    """
    Route to the respective intent module code
    """
    
    intent = dialog.get_intent(intent_request)
    intent_name = intent['name']
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    
    
    # Default dialog state is set to delegate
    next_state = dialog.delegate(active_contexts, session_attributes, intent)
    
    
    # Dispatch to the respective intent's handler
    if intent_name == 'WeightLossIntent':
        next_state = weight_loss_intent.handler(intent_request)
    if intent_name == 'WeightGainIntent':
        next_state = weight_gain_intent.handler(intent_request)
        
    return next_state


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    # os.environ['TZ'] = 'America/New_York'
    # time.tzset()
    # logger.debug(event)
    # print(event)

    return dispatch(event)
