import dialogstate_utils as dialog
import json
import random as random
from utils import calculate_bmi, calculate_tdee, calculate_nutrition,calculate_amount
import gain_utils as gu
from food import get_food


def compose_weight_gain(height, weight, gender, activity_level, age,intent_request, session_attributes):
    status = calculate_bmi(weight, height)
    calorie_per_day = calculate_tdee(
        weight, height, age, gender, activity_level)
    messages = []

    calorie_subtracted = calorie_per_day + 300
    weight = float(weight)
    protein = gu.calculate_protein_gain(weight*2.2)
    fat = gu.calculate_fat_gain(calorie_subtracted)
    carbs = gu.caculate_carb_gain(calorie_subtracted, protein, fat)

    response1 = f'You are {status} and you need to consume {round(calorie_per_day,2)} calore per day to maintain this weight.'

    response2 = f'According to your goal, to gain weight you need to consume {round(calorie_subtracted,)} calorie per day, {round(protein,2)} gm protein per day, {round(fat, 2)} gm fat per day and {round(carbs,2)} carb per day'

    response3 = 'What are the foods you eat in a full day? Enter along with amount. (eg. 1 cuprice, 2 banana)'
    messages.append({'contentType': 'PlainText', 'content': response1})

    messages.append({'contentType': 'PlainText', 'content': response2})
    messages.append({'contentType': 'PlainText', 'content': response3})
    
    intent_request = dialog.set_session_attribute(intent_request, 'calorie_subtracted',calorie_subtracted)
    intent_request = dialog.set_session_attribute(intent_request, 'fat',fat)
    intent_request = dialog.set_session_attribute(intent_request, 'protein',protein)
    intent_request = dialog.set_session_attribute(intent_request, 'carbs',carbs)
    

    return messages, intent_request


def compose_food(food,intent_request):
    user_input = food.split(',')
    menu = get_food()
    response = calculate_nutrition(user_input, menu)
    messages = []
    
    calorie = round(float(dialog.get_session_attribute(intent_request,'calorie_subtracted')),2)
    protein =round( float(dialog.get_session_attribute(intent_request,'protein')),2)
    carbs = round(float(dialog.get_session_attribute(intent_request,'carbs')),2)
    fat = round(float(dialog.get_session_attribute(intent_request,'fat')),2)
    
    
    diff_calorie = abs(response[0]- calorie)
    diff_protein = abs(response[1]- protein)
    diff_carbs = abs(response[2]- carbs)
    diff_fat = abs(response[3]- fat)
    
    
    
    amount_info = calculate_amount(diff_calorie,menu,user_input)
    
    response_text = f'To gain weight you should adjust '
    
    for key, value in amount_info.items():
        response_text += f'{value}g of {key} '
    
    response_text += 'to your daily food.'
    
    
    messages.append({'contentType': 'PlainText', 'content': response_text})
    
    
    return messages


def handler(intent_request):
    intent = dialog.get_intent(intent_request)
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)

    height = dialog.get_slot('Height', intent)
    weight = dialog.get_slot('Weight', intent)
    gender = dialog.get_slot('Gender', intent)
    activity_level = dialog.get_slot('ActivityLevel', intent)
    age = dialog.get_slot('Age', intent)
    food = dialog.get_slot('Food', intent)

    if height is None:
        dialog.elicit_slot(
            'Height', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': "Enter your height in meters"}])
    if weight is None:
        dialog.elicit_slot(
            'Weight', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': "Enter your weight in KG"}])
    if gender is None:
        dialog.elicit_slot(
            'Gender', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': "What is your gender?"}])
    if activity_level is None:
        dialog.elicit_slot(
            'ActivityLevel', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': "What is your activity level?"}])
    if age is None:
        dialog.elicit_slot(
            'Age', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': "What is your age?"}])

    if height and weight and gender and activity_level and age:
        if food is None:
            response, intent_request = compose_weight_gain(
                height, weight, gender, activity_level, age,intent_request, session_attributes)
            
            session_attributes = dialog.get_session_attributes(intent_request)
            return dialog.elicit_slot(
                'Food', active_contexts,
                session_attributes, intent,
                response)
        else:
            response = compose_food(food, intent_request)
            print(response)
            return dialog.close(active_contexts, session_attributes, intent, response)
            
    return dialog.delegate(active_contexts, session_attributes, intent)
