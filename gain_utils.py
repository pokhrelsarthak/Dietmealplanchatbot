from random import uniform

def calculate_protein_gain(weight):
    weight = float(weight)
    return 0.9*weight
    
def calculate_fat_gain(calorie):
    calorie = float(calorie)
    percent = uniform(0.2,0.3)
    return percent*calorie/9
    
def caculate_carb_gain(calorie,protein,fat):
    calorie = float(calorie)
    protein = float(protein)
    fat = float(fat)
    return (calorie-protein*4-fat*9)/4