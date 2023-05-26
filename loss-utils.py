from random import uniform

def calculate_protein_loss(weight):
    weight = float(weight)
    return 1.3*weight
    
def calculate_fat_loss(calorie):
    calorie = float(calorie)
    percent = uniform(0.15,0.25)
    return percent*calorie/9
    
def caculate_carb_loss(calorie,protein,fat):
    calorie = float(calorie)
    protein = float(protein)
    fat = float(fat)
    return (calorie-protein*4-fat*9)/4