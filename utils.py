def calculate_bmi(weight, height):
    weight = float(weight)
    height = float(height)
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_tdee(weight, height, age, gender, activity_level):
    bmr = 0.0
    height = float(height)
    age = int(age)
    weight = float(weight)
    
    activity_level = float(activity_level)
    
    height = height * 100
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    tdee = bmr * activity_level
    return tdee



def calculate_nutrition(user_input, menu):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for item in user_input:
        amount, name = item.split(' ', 1)
        name = name.lower().split(" ")[-1]
        for food_name, food_info in menu.items():
            # print(f'{name.lower()} ; {food_name.lower()}')
            if name.lower() in food_name.lower():
                if 'g' in amount.lower():
                    multiplier = float(''.join(filter(str.isdigit, amount)))
                    multiplier = multiplier/100
                    # print(multiplier)
                else:
                    multiplier = float(amount)
                    # print(multiplier)

                total_calories += food_info["calories"] * multiplier
                total_protein += food_info["protein"] * multiplier
                total_carbs += food_info["carbs"] * multiplier
                total_fat += food_info["fat"] * multiplier

    return round(total_calories,2), round(total_protein,2), round(total_carbs,2), round(total_fat,2)
    
def calculate_amount(diff, menu):
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    calorie_diff = diff[0]
    protein_diff = diff[1]
    carbs_diff= diff[2]
    fat_diff = diff[3]

    for item in user_input:
        amount, name = item.split(' ', 1)
        name = name.lower().split(" ")[-1]
        for food_name, food_info in menu.items():
            if name.lower() in food_name.lower():
                if 'g' in amount.lower():
                    multiplier = float(''.join(filter(str.isdigit, amount)))
                    multiplier = multiplier/100
                    # print(multiplier)
                else:
                    multiplier = float(amount)
                    # print(multiplier)

                total_calories_amount = food_info["calories"] * multiplier
                total_protein += food_info["protein"] * multiplier
                total_carbs += food_info["carbs"] * multiplier
                total_fat += food_info["fat"] * multiplier

    return round(total_calories,2), round(total_protein,2), round(total_carbs,2), round(total_fat,2)
    

def calculate_amount(calorie_diff, menu,user_input):
    multiplier = 0
    amount_value = 0

    amount_info = {}

    for item in user_input:
        amount, name = item.split(' ', 1)
        name = name.lower().split(" ")[-1]
        for food_name, food_info in menu.items():
            if name.lower() in food_name.lower():
                if 'g' in amount.lower():
                    multiplier =  float(amount[:-1])
                    multiplier = multiplier/100
                    # print(multiplier)
                    amount_value = float(amount[:-1])
                else:
                    multiplier= float(amount)
                    amount_value= float(amount)
                amount_info[name] = round((calorie_diff/food_info['calories'] ) * amount_value,2)
    return amount_info