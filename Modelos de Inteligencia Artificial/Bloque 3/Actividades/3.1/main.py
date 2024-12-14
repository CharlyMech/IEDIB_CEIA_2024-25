from clips import Environment, Symbol

def calculate_bmr(weight, height, age, gender):
   base = 10 * weight + 6.25 * height - 5 * age
   return base + 5 if gender == 'male' else base - 161

def validate_training_data(gender, weekly_freq, intensity, strength_training, cardio_training, objective):
   valid_objectives = ['lose', 'maintain', 'gain']
   valid_genders = ['male', 'female']
   if gender not in valid_genders:
      raise ValueError(f'Gender must be one of {valid_genders}, got {gender}.')
   if not (0 <= weekly_freq <= 7):
      raise ValueError(f'Weekly frequency value must be between 0 and 7, got {weekly_freq}.')
   if not (0 <= intensity <= 10):
      raise ValueError(f'Intensity value must be between 0 and 10, got {intensity}.')
   if strength_training not in [0, 1]:
      raise ValueError(f'Strenght training value must be 0 or 1, got {strength_training}.')
   if cardio_training not in [0, 1]:
      raise ValueError(f'Cardio training value must be 0 or 1, got {cardio_training}.')
   if objective not in valid_objectives:
      raise ValueError(f'Objective value must be one of {valid_objectives}, got {objective}.')


def main():
   TEMPLATE_STRING = '''
   (deftemplate training
      (slot weekly_freq (type INTEGER))
      (slot intensity (type INTEGER))
      (slot strength_training (type INTEGER))
      (slot cardio_training (type INTEGER))
      (slot objective (type SYMBOL))
      (slot calories (type FLOAT))
   )
   '''

   RULE_LOSE_WEIGHT = '''
   (defrule lose-weight
      "Start incorporating a caloric deficit to the diet."
      (training (objective lose))
      =>
      (printout t "- Start eating healty, incorporating a caloric deficit (e.g. -300kcals) alongside a consistent training routine." crlf)
   )
   '''

   RULE_MAINTAIN_WEIGHT = '''
   (defrule maintain-weight
      "Maintain current weight with a balanced diet."
      (training (objective maintain) (calories ?c))
      =>
      (printout t "- Maintain your current weight by eating approximately: " ?c "kcal per day with healty diet and training." crlf)
   )
'''

   RULE_GAIN_WEIGHT = '''
   (defrule lose-weight
      "Start incorporating a caloric habit to the diet."
      (training (objective gain))
      =>
      (printout t "- Start a bulk (caloric habit (e.g. +300kcals)) alongside strength training and less cardio." crlf)
   )
   '''

   RULE_START_TRAINING = '''
   (defrule recommend-training
      "Recommend start training."
      (training (weekly_freq 0))
      =>
      (printout t "- Start training at least 3 times a week, combining cardio, light weighted strength training and eat healthy." crlf)
   )
   '''

   RULE_MORE_STRENGTH = '''
   (defrule recommend-more-strength
      "Recommend adding strength training to the routine."
      (training (strength_training 0) (weekly_freq ?f &: (< ?f 3) &: (> ?f 0)))
      =>
      (printout t "- You should incorporate strength training into your routine to build muscle." crlf)
   )
   '''

   RULE_MORE_CARDIO = '''
   (defrule recommend-more-cardio
      "Recommend adding cardio training to the routine."
      (training (cardio_training 0) (weekly_freq ?f &: (< ?f 3) &: (> ?f 0)))
      =>
      (printout t "- You should incorporate cardio training into your routine to improve cardio vascular health and breathing technique." crlf)
   )
   '''

   env = Environment()
   # These rules are very basic and might be incomplete for a real case
   env.build(TEMPLATE_STRING)
   env.build(RULE_START_TRAINING)
   env.build(RULE_MORE_STRENGTH)
   env.build(RULE_MORE_CARDIO)
   env.build(RULE_LOSE_WEIGHT)
   env.build(RULE_MAINTAIN_WEIGHT)
   env.build(RULE_GAIN_WEIGHT)
   

   print('- Welcome to your personal training assistant! -')
   print('Please fill the following information (look carefully the suitable answers)')

   print('Please fill in your details:')
   try:
      weight = float(input('Enter your weight (kg): '))
      height = float(input('Enter your height (cm): '))
      age = int(input('Enter your age (years): '))
      gender = input('Enter your gender (male/female): ').strip().lower()
      weekly_freq = int(input('Enter weekly training frequency (0-7): '))
      intensity = int(input('Enter intensity level (1-10): '))
      strength_training = int(input('Strength training? (1 for Yes, 0 for No): '))
      cardio_training = int(input('Cardio training? (1 for Yes, 0 for No): '))
      objective = input('Enter your goal (lose/manitain/gain): ').strip().lower()
      validate_training_data(gender, weekly_freq, intensity, strength_training, cardio_training, objective)

      calories = calculate_bmr(weight = weight, height = height, age = age, gender = gender)

      print(f'- Your calorie intake: ~{calories}')

      template = env.find_template('training')
      fact = template.assert_fact(
         weekly_freq=weekly_freq,
         intensity=intensity,
         strength_training=strength_training,
         cardio_training=cardio_training,
         objective=Symbol(objective),
         calories=calories
      )
      print(f"Asserted fact: {fact}")
      print('\nHere you have your recommendations:')
      env.run()
   except ValueError as v_error:
      print(f'Invalid input: {v_error}')

if __name__ == '__main__':
	main()