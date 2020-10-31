
def max_num(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort(reverse=True)
    return nums[0]
     
num1 = float(input('ENTER FIRST NUMBER: '))
op = input('ENTER OPERATOR: ')
num2 = float(input("ENTER SECOND NUMBER: "))


def calculate(first, operation, second):
    if(operation == '+'):
        print(first + second)
    elif(operation == '-'):
        print(first - second)
    elif(operation == '/'):
        print(first / second)
    elif(operation == "*"):
        print(first * second)
    else:
        print('invalid operator')

calculate(num1, op, num2)

secret_word = 'jojo'
guess = ""
limit = 3
tries = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses) :
    if(tries < limit):
        guess = input('ENTER GUESS: ')
        tries = tries + 1
    else:
        out_of_guesses = True
   
if(out_of_guesses == True):
    print('Better luck next time')
else:
    print("YOU WON THE GAME!!")


def raise_to_power(base, power):
    result = 1
    for i in range(power):
        result = result * power
    return result


def translator(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if(letter.isupper()):
                translation = translation + 'G'
            else:
                translation = translation + 'g';
        else:
            translation = translation + letter
    return translation


try:
    chum = 2/0
    number = int(input("ENTER A NUMBER: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('invalid input')

fruits = open('fruits.txt', 'w')
fruits.write('\nwatermelon')
fruits.write('\napple')
fruits.write('\nplum')
fruits.close()

import info 
print(info.feet_in_mile)


from Student import Student

jake = Student("Sahil", "Computer Science", 3.68, False)

print(jake.gpa)

from Question import Question

question_prompts = [
    "What color is the sky?\n(a) Blue\n(b) Red\n(c) Purple\n\n",
    "What color are apples?\n(a) Red\n(b) Blue\n(c) Green\n\n",
    "What color are bananas?\n(a) Teal\n(b) Yellow\n(c) Black\n\n",
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'a'),
    Question(question_prompts[2], 'b'),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print('You got ' + str(score) + '/' + str(len(questions)))
   

run_test(questions)


