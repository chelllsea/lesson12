import time
import random

print('*' * 50)

print('Magic 8 Ball: ')

print()

question = input("What's your question? ")

print()

print("...shaking...")
time.sleep(2)

print()
print('...still shaking...')
time.sleep(2)

print()
print('...determining...')
time.sleep(2)

choice = random.randint(1,6)

if choice == 1:
	print()
	print("Sure.")

elif choice == 2:
	print()
	print("Ask again.")

elif choice == 3:
	print()

print('*' * 50)