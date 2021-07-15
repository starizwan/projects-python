# concatenate a string: 3 ways to do 
# 1. print("My name is " + first_name)
# 2. print("I am {}".format(first_name))
# 3. print(f"My name is {first_name}")

food = input("Food: ")
name = input("Name : ")
adjective = input("Adjective ")
noun = input("Noun : ")
verb1, verb2, verb3 = input("Verb 1, 2 & 3: ").split()


output = f'''It was {food} day at school, and {name} was super {adjective} for lunch. 
But when she went outside to eat, a {noun} stole her {food}! {name} chased 
the {noun} all over school. She {verb1}, {verb2}, and {verb3} through 
the playground. Then she tripped on her shoelace and the {noun} escaped! 
Luckily, {name}’s friends were willing to share their {food} with her.'''

print(output)