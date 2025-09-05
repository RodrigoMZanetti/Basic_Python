weight=float(input('What is your weight (kg)? '))
height=float(input('What is your height (m)? '))
bmi=(weight/(height**2))
if bmi<18.5:
    print(f'You Body Mass Index is {bmi:.1f} and is classified as: Underweight')
elif 18.5 <= bmi < 25:
    print(f'You Body Mass Index is {bmi:.1f} and is classified as: Normal')
elif 25 <= bmi < 30:
    print(f'You Body Mass Index is {bmi:.1f} and is classified as: Overweight')
elif 30 <= bmi < 40:
    print(f'You Body Mass Index is {bmi:.1f} and is classified as: Obesity')
elif bmi >= 40:
    print(f'You Body Mass Index is {bmi:.1f} and is classified as: Morbid obesity')


