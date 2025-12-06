"""
module
"""

class Day1Dial:
    """
    A 100 digit dial that can be rotated and tracks how often it lands on zero after a rotation.
    """
    dial_size = 100
    zero_count = 0
    zero_click = 0
    def __init__(self, position):
        self.position = position

    def normalised_position(self):
        """Numbers roll, 0-99"""
        self.position %= Day1Dial.dial_size

    def check_zero_count(self):
        """Increments if rotation landed on zero"""
        if self.position == 0:
            self.zero_count += 1

    def rotate_left(self, val:int):
        "Rotate the dial left (dec)"
        self.position -= val
        self.normalised_position()
        self.check_zero_count()

    def rotate_right(self, val:int):
        "Rotate the dial right (inc)"
        self.position += val
        self.normalised_position()
        self.check_zero_count()

    def receive_instruction(self, instruction:str):
        "Input a rotation instruction. E.g. 'R34'"
        direction = instruction[0]
        value = int(instruction[1:])

        if direction == 'L':
            self.rotate_left(value)
        elif direction == 'R':
            self.rotate_right(value)

    def receive_instructions(self, instructions):
        """"""
        for instruction in instructions:
            self.receive_instruction(instruction)