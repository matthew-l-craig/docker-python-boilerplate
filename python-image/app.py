import os
from time import sleep
print("This is my first image.")
print(f"Current working directory: {os.getcwd()}")
print(os.listdir())

name = input("What's your name?")

print(f"Hello, {name}! What a beautiful name! It really suits you.")