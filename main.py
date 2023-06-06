userStart = "y"
gender = ""
genderInt = 0
weight = 0.0
heightft = 0
heightin = 0
age = 0
activityLevel = 0.0
validLvl = True

def harrisBenedictTDEE(genderInt, weight, height, age, activityLevel):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54

        if genderInt == 1:
            BMR = 88.362 + (13.397 * kgWeight) + (4.799 * cmHeight) - (5.677 * age)
            TDEE = BMR * activityLevel
            return TDEE
        elif genderInt == 2:
            BMR = 447.593 + (9.247 * kgWeight) + (3.098 * cmHeight) - (4.330 * age)
            TDEE = BMR * activityLevel
            return TDEE

def harrisBenedictBMR(genderInt, weight, height, age):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54

        if genderInt == 1:
            BMR = 88.362 + (13.397 * kgWeight) + (4.799 * cmHeight) - (5.677 * age)
            return BMR
        elif genderInt == 2:
            BMR = 447.593 + (9.247 * kgWeight) + (3.098 * cmHeight) - (4.330 * age)
            return BMR             

def mifflinStJeorBMR(genderInt, weight, height, age):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54        

        if genderInt == 1:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) + 5
            return BMR
        elif genderInt == 2:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) - 161
            return BMR

def mifflinStJeorTDEE(genderInt, weight, height, age, activityLevel):
        
        kgWeight = weight *.45359237
        cmHeight = height * 2.54        

        if genderInt == 1:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) + 5
            TDEE = BMR * activityLevel
            return TDEE
        elif genderInt == 2:
            BMR = (10 * kgWeight) + (6.25 * cmHeight) - (5 * age) - 161
            TDEE = BMR * activityLevel
            return TDEE       


print("\n-----MACRO NURTITION CALCULATOR-----")
print("Welcome to the macro nutrition calculator.")
userStart = input("Would you like to begin? (y/n)")


while userStart.upper() != "n".upper():
    try:
        genderInput = input("\nChoose your gender:\nEnter 1 for Male or 2 for Female: ")
        genderInt = int(genderInput)
    except ValueError:
        print("Invalid number, please enter in 1 or 2.")

    try:
        weightInput = input("\nHow much do you weigh? (in pounds): ")
        weight = float(weightInput)
    except ValueError:
        print("Invalid weight, please enter in a number.")

    try:
        ageInput = input("\nWhat is your age? (in years): ")
        age = int(ageInput)
    except ValueError:
        print("Invalid age, please enter in a number.") 

    print("\nI will ask your heigh in feet first, and then inches\nFor example: I am 6 feet 4 inches tall, so I would enter in '6' for feet and '4' for inches")

    try:
        heightFtInput = input("What is your height in feet?: ")
        heightft = int(heightFtInput)
    except ValueError:
        print("Invalid height, please enter in a number.")   

    try:
        heightInInput = input("What is your height in inches?: ")
        heightin = int(heightInInput)
    except ValueError:
        print("Invalid height, please enter in a number.")  

    height = heightin + (heightft * 12) 

    validLvl = False
    while validLvl != True:
        try:
            activityLvlInput = input("\nPlease select a number that corresponds with your activity level:\nLittle or no exercise, desk job: 1\nLight exercise or sports 1-3 days a week: 2\nModerate exercise or sports 3-5 days a week: 3\nHard exercise or sports 6-7 days a week: 4\nVery hard exercise or sports, physical job or training twice a day: 5\nActivity Level: ")
            activityLevel = float(activityLvlInput)
            if activityLevel >= 1 and activityLevel <= 5:
                if activityLevel == 1:
                    activityLevel = 1.2
                    validLvl = True
                elif activityLevel == 2:
                    activityLevel = 1.375
                    validLvl = True
                elif activityLevel == 3:
                    activityLevel = 1.55
                    validLvl = True
                elif activityLevel == 4:
                    activityLevel = 1.725
                    validLvl = True
                elif activityLevel == 5:
                    activityLevel = 1.9
                    validLvl = True
                else:
                    print("\nPlease enter in a number between 1 and 5.\n")
                    validLvl = False                
        except ValueError:
            print("Invalid input, please enter in a number.")

    validGoal = False
    while validGoal != True:
        try:
            goalInput = input("\nSelect the number that corresponds with your choice:\n\nWould you like to:\nLose Weight: 1\nGain Weight: 2\nMaintain Weight: 3\nWhat would you like to do: ")
            goalChoice = int(goalInput)
            if goalChoice >= 1 and goalChoice <=3:
                validGoal = True
            else:
                print("\nPlease enter a number between 1 and 3\n")
                validGoal = False
        except ValueError:
            print("Invalid number, please choose a number between 1 and 3")





    hbTDEE = harrisBenedictTDEE(genderInt, weight, height, age, activityLevel)
    msTDEE = mifflinStJeorTDEE(genderInt, weight, height, age, activityLevel)
    hbBMR = harrisBenedictBMR(genderInt, weight, height, age)
    msBMR = mifflinStJeorBMR(genderInt, weight, height, age)

    BMR = (hbBMR + msBMR) // 2
    BMRprint = round(BMR, 2)
    TDEE = (hbTDEE + msTDEE) // 2
    TDEEprint = round(TDEE, 2)

    if goalChoice == 1:
        dailyCal = TDEE - 500

        dailyCarbs = (.4 * dailyCal) / 4
        DCprint = round(dailyCarbs, 2)

        dailyProtien = (.3 * dailyCal) / 4
        DPprint = round(dailyProtien, 2) 

        dailyFat = (.3 * dailyCal) / 9
        DFprint = round(dailyFat, 2)


    elif goalChoice == 2:   
        dailyCal = TDEE + 500

        dailyCarbs = (.5 * dailyCal) / 4 
        DCprint = round(dailyCarbs, 2)

        dailyProtien = (.3 * dailyCal) / 9
        DPprint = round(dailyProtien, 2) 

        dailyFat = (.2 * dailyCal) / 9
        DFprint = round(dailyFat, 2)


    elif goalChoice == 3:
        dailyCal = TDEE

        DCprint = round(dailyCarbs, 2)
        dailyCarbs = (.45 * dailyCal) / 4
        
        DPprint = round(dailyProtien, 2) 
        dailyProtien = (.25 * dailyCal) / 4

        dailyFat = (.3 * dailyCal) / 9 
        DFprint = round(dailyFat, 2)

    print("\nHere is your macronutrient goals:\nYou burn ", BMRprint, " calories everyday without any exercise\nYou burn ", TDEEprint, " calories every day with your amount of exercise\nDepending on if you want to lose, gain, or maintain, you should eat ", dailyCal, " calories a day.\n\nBelow are the macronutrients of how you should split those calories up:\nProtien: ", DPprint, " grams of protien per day\nCarbohydrates: ", DCprint, " grams of carbohydrates per day\nFat: ", DFprint, "grams of fats per day" )




    userStart = "n"





