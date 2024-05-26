#Print in color
print( '=== Adventure Story!===')
name = input('What is your name? ')
print(f'Welcome {name}! You are about to embark on a great' "\033[31m" " adventure" "\033[0m" ". ")
print(f"{name}, You'll be asked a series of questions to determine your adventure.")
print()
print("Let's begin!")
adventure = input('What is your favorite adventure? ')
likes = input(f'What do you like about {adventure} ? ')
friend = input('What is the name of your best friend? ')
food = input('What is your favorite food? ')
print()
print(
f"Once upon a time, {name} and {friend} went on an adventure. It was a great bonding experience for them as they got to spend time together." 
f"They were both so excited to go to {adventure} because it meant {likes}." 
f"They packed their food, {food}, and set out to the park where the other participants were waiting." 
f"One hour into the {adventure}," "\033[31m" " a storm started" "\033[0m" " and they were separated from the group."
f" After the storm ended, {friend} was no where to be found. A search party was sent out to look for her but she was not" "\033[31m" " found" "\033[0m" " ." 
f"{name} thinks about {friend} all the time. And has not gone on another {adventure} since {friend}'s" "\033[31m" " disappearance" "\033[0m" "."	
)
