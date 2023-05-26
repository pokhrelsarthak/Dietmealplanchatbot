import json


def get_food():
    menu = {
        "Salmon": {
            "calories": 206,
            "protein": 22,
            "carbs": 0,
            "fat": 13,
            "amount": "100g"
        },
        "Egg": {
            "calories": 78,
            "protein": 6,
            "carbs": 0.6,
            "fat": 5,
            "amount": "1 large egg"
        },
        "Greek Yogurt": {
            "calories": 133,
            "protein": 10,
            "carbs": 6,
            "fat": 0,
            "amount": "170g"
        },
        "Quinoa": {
            "calories": 120,
            "protein": 4.4,
            "carbs": 21,
            "fat": 1.9,
            "amount": "100g cooked"
        },
        "Spinach": {
            "calories": 23,
            "protein": 2.9,
            "carbs": 3.6,
            "fat": 0.4,
            "amount": "100g"
        },
        "Almonds": {
            "calories": 579,
            "protein": 21,
            "carbs": 22,
            "fat": 49,
            "amount": "100g"
        },
        "Oats": {
            "calories": 153,
            "protein": 5,
            "carbs": 27,
            "fat": 2,
            "amount": "40g"
        },
        "Broccoli": {
            "calories": 55,
            "protein": 3.7,
            "carbs": 11,
            "fat": 0.6,
            "amount": "100g"
        },
        "Sweet Potato": {
            "calories": 86,
            "protein": 1.6,
            "carbs": 20,
            "fat": 0.1,
            "amount": "100g"
        },
        "Rice": {
            "calories": 130,
            "protein": 2.7,
            "carbs": 28.1,
            "fat": 0.3,
            "amount": "1 cup cooked"
        },
        "Dal (Lentils)": {
            "calories": 116,
            "protein": 9,
            "carbs": 20,
            "fat": 0.4,
            "amount": "100g cooked"
        },
        "Banana": {
            "calories": 96,
            "protein": 1.2,
            "carbs": 23,
            "fat": 0.2,
            "amount": "1 medium-sized"
        },
        "Paneer": {
            "calories": 265,
            "protein": 18,
            "carbs": 4,
            "fat": 21,
            "amount": "100g"
        },
        "Chapati (Roti)": {
            "calories": 104,
            "protein": 3.4,
            "carbs": 20.8,
            "fat": 1.6,
            "amount": "1 medium-sized"
        },
        "Idli": {
            "calories": 39,
            "protein": 1.8,
            "carbs": 8,
            "fat": 0.4,
            "amount": "1 piece"
        },
        "Dosa": {
            "calories": 133,
            "protein": 2.6,
            "carbs": 27,
            "fat": 1.5,
            "amount": "1 medium-sized"
        },
        "Poha": {
            "calories": 250,
            "protein": 4,
            "carbs": 55,
            "fat": 1.2,
            "amount": "1 cup"
        },
        "Upma": {
            "calories": 235,
            "protein": 5,
            "carbs": 37,
            "fat": 6,
            "amount": "1 cup"
        },
        "Mango": {
            "calories": 60,
            "protein": 0.8,
            "carbs": 15,
            "fat": 0.4,
            "amount": "1 medium-sized"
        },
        "Fish Curry": {
            "calories": 200,
            "protein": 18,
            "carbs": 8,
            "fat": 10,
            "amount": "1 serving"
        },
        "Oatmeal": {
            "calories": 150,
            "protein": 5,
            "carbs": 27,
            "fat": 2,
            "amount": "1/2 cup (uncooked)"
        },
        "Greek Salad": {
            "calories": 150,
            "protein": 5,
            "carbs": 10,
            "fat": 11,
            "amount": "1 serving"
        },
        "Grilled Chicken Breast": {
            "calories": 165,
            "protein": 31,
            "carbs": 0,
            "fat": 3.6,
            "amount": "4 oz (cooked)"
        },
        "Steamed Vegetables": {
            "calories": 50,
            "protein": 2,
            "carbs": 10,
            "fat": 0.5,
            "amount": "1 cup"
        },
        "Quinoa Sa": {
            "calories": 220,
            "protein": 8,
            "carbs": 39,
            "fat": 4,
            "amount": "1 serving"
        },
        "Avocado": {
            "calories": 160,
            "protein": 2,
            "carbs": 9,
            "fat": 15,
            "amount": "1 medium-sized"
        },
        "Mixed Nuts": {
            "calories": 170,
            "protein": 6,
            "carbs": 5,
            "fat": 15,
            "amount": "1/4 cup"
        },
        "Quinoa Bowl": {
            "calories": 300,
            "protein": 12,
            "carbs": 50,
            "fat": 6,
            "amount": "1 serving"
        },
        "Green Smoothie": {
            "calories": 150,
            "protein": 5,
            "carbs": 25,
            "fat": 3,
            "amount": "1 glass"
        },
        "Chickpeas": {
            "calories": 269,
            "protein": 14.5,
            "carbs": 45,
            "fat": 4.2,
            "amount": "1 cup (cooked)"
        },
        "Sprouts": {
            "calories": 81,
            "protein": 6,
            "carbs": 15,
            "fat": 0.6,
            "amount": "1 cup"
        },
        "Masoor Dal (Red Lentils)": {
            "calories": 352,
            "protein": 24,
            "carbs": 63,
            "fat": 1.2,
            "amount": "1 cup (cooked)"
        },
        "Chana Masala (Chickpea Curry)": {
            "calories": 286,
            "protein": 10,
            "carbs": 50,
            "fat": 6,
            "amount": "1 cup (cooked)"
        },
        "Methi (Fenugreek) Paratha": {
            "calories": 177,
            "protein": 5,
            "carbs": 31,
            "fat": 4,
            "amount": "1 medium-sized"
        },
        "Baingan Bharta": {
            "calories": 160,
            "protein": 2,
            "carbs": 9,
            "fat": 14,
            "amount": "1 cup"
        },
        "Tofu Tikka Masala": {
            "calories": 245,
            "protein": 14,
            "carbs": 10,
            "fat": 17,
            "amount": "1 cup"
        },
        "Sattu Drink": {
            "calories": 150,
            "protein": 9,
            "carbs": 22,
            "fat": 2,
            "amount": "1 glass"
        },
        "Bajra Roti (Pearl Millet Flatbread)": {
            "calories": 86,
            "protein": 2,
            "carbs": 17,
            "fat": 1,
            "amount": "1 medium-sized"
        },
        "Mung Dal (Split Green Gram)": {
            "calories": 105,
            "protein": 7,
            "carbs": 19,
            "fat": 0.4,
            "amount": "1/2 cup (cooked)"
        },
        "Tandoori Chicken": {
            "calories": 165,
            "protein": 25,
            "carbs": 0,
            "fat": 7,
            "amount": "1 piece (120g)"
        },
        "Apple": {
            "calories": 52,
            "protein": 0.3,
            "carbs": 14,
            "fat": 0.2,
            "amount": "1 medium-sized"
        },
        "Orange": {
            "calories": 62,
            "protein": 1.2,
            "carbs": 15,
            "fat": 0.2,
            "amount": "1 medium-sized"
        },
        "Strawberry": {
            "calories": 29,
            "protein": 0.7,
            "carbs": 7,
            "fat": 0.3,
            "amount": "1 cup"
        },
        "Pineapple": {
            "calories": 50,
            "protein": 0.5,
            "carbs": 13,
            "fat": 0.1,
            "amount": "1 cup (chunks)"
        },
        "Watermelon": {
            "calories": 30,
            "protein": 0.6,
            "carbs": 8,
            "fat": 0.2,
            "amount": "1 cup (cubes)"
        },
        "Grapes": {
            "calories": 69,
            "protein": 0.7,
            "carbs": 18,
            "fat": 0.2,
            "amount": "1 cup"
        },
        "Kiwi": {
            "calories": 61,
            "protein": 1.1,
            "carbs": 15,
            "fat": 0.5,
            "amount": "1 medium-sized"
        },
        "Blueberries": {
            "calories": 57,
            "protein": 0.7,
            "carbs": 14,
            "fat": 0.3,
            "amount": "1 cup"
        },
        "Pomegranate": {
            "calories": 83,
            "protein": 1.7,
            "carbs": 19,
            "fat": 1.2,
            "amount": "1 medium-sized"
        }
    }

    return menu
