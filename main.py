from dial import Day1Dial
from utils import get_input

day1_dial = Day1Dial(50)
day1_dial.receive_instructions(get_input("day1.txt"))
print(f"Day 1.1: {day1_dial.zero_count}")
print(f"Day 1.2: {day1_dial.zero_click}")
