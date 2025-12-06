"""
Docstring for test_dial
"""
from dial import Day1Dial

class TestDay1Dial:
    """d"""

    def test_init(self):
        """s"""
        day1_dial = Day1Dial(0)
        assert day1_dial.position == 0
        assert day1_dial.zero_count == 0
        assert day1_dial.dial_size == 100

        day1_dial = Day1Dial(55)
        assert day1_dial.position == 55
        assert day1_dial.zero_count == 0
        assert day1_dial.dial_size == 100

    def test_zero_count(self):
        """s"""
        day1_dial = Day1Dial(0)
        day1_dial.zero_count = 0

        assert day1_dial.zero_count == 0

        day1_dial.check_zero_count()
        assert day1_dial.zero_count == 1

        day1_dial.check_zero_count()
        assert day1_dial.zero_count == 2

        day1_dial.check_zero_count()
        day1_dial.check_zero_count()
        day1_dial.check_zero_count()
        day1_dial.check_zero_count()
        day1_dial.check_zero_count()
        assert day1_dial.zero_count == 7

    def test_normalise(self):
        """s"""
        day1_dial = Day1Dial(0)

        assert day1_dial.position == 0

        day1_dial.normalised_position()
        assert day1_dial.position == 0

        day1_dial.position = 33
        day1_dial.normalised_position()
        assert day1_dial.position == 33

        day1_dial.position = 99
        day1_dial.normalised_position()
        assert day1_dial.position == 99

        day1_dial.position = -5
        day1_dial.normalised_position()
        assert day1_dial.position == 95

        day1_dial.position = 112
        day1_dial.normalised_position()
        assert day1_dial.position == 12

        day1_dial.position = 314
        day1_dial.normalised_position()
        assert day1_dial.position == 14

        day1_dial.position = -506
        day1_dial.normalised_position()
        assert day1_dial.position == 94

    def test_rotate_right(self):
        """s"""
        day1_dial = Day1Dial(0)

        assert day1_dial.position == 0

        day1_dial.rotate_right(1)
        assert day1_dial.position == 1

        day1_dial.position = 0
        day1_dial.rotate_right(11)
        assert day1_dial.position == 11

        day1_dial.position = 0
        day1_dial.rotate_right(1)
        day1_dial.rotate_right(2)
        day1_dial.rotate_right(4)
        day1_dial.rotate_right(8)
        assert day1_dial.position == 15

        day1_dial.position = 0
        day1_dial.rotate_right(120)
        assert day1_dial.position == 20

        day1_dial.position = 0
        day1_dial.rotate_right(555)
        assert day1_dial.position == 55

    def test_rotate_left(self):
        """s"""
        day1_dial = Day1Dial(0)

        assert day1_dial.position == 0

        day1_dial.rotate_left(1)
        assert day1_dial.position == 99

        day1_dial.position = 0
        day1_dial.rotate_left(11)
        assert day1_dial.position == 89

        day1_dial.position = 0
        day1_dial.rotate_left(1)
        day1_dial.rotate_left(2)
        day1_dial.rotate_left(4)
        day1_dial.rotate_left(8)
        assert day1_dial.position == 85

        day1_dial.position = 0
        day1_dial.rotate_left(120)
        assert day1_dial.position == 80

        day1_dial.position = 0
        day1_dial.rotate_left(555)
        assert day1_dial.position == 45

    def test_receive_instruction(self):
        """s"""
        day1_dial = Day1Dial(0)
        day1_dial.receive_instruction("R55")
        assert day1_dial.position == 55
        assert day1_dial.zero_count == 0

        day1_dial = Day1Dial(0)
        day1_dial.receive_instruction("R50")
        assert day1_dial.position == 50
        assert day1_dial.zero_count == 0
        day1_dial.receive_instruction("R50")
        assert day1_dial.position == 0
        assert day1_dial.zero_count == 1
        day1_dial.receive_instruction("R50")
        assert day1_dial.position == 50
        assert day1_dial.zero_count == 1

        day1_dial = Day1Dial(0)
        day1_dial.receive_instruction("L20")
        assert day1_dial.position == 80
        assert day1_dial.zero_count == 0

        day1_dial = Day1Dial(0)
        day1_dial.receive_instruction("L25")
        assert day1_dial.position == 75
        assert day1_dial.zero_count == 0
        day1_dial.receive_instruction("L75")
        assert day1_dial.position == 0
        assert day1_dial.zero_count == 1
        day1_dial.receive_instruction("L10")
        assert day1_dial.position == 90
        assert day1_dial.zero_count == 1

        day1_dial = Day1Dial(0)
        day1_dial.receive_instruction("L15")
        assert day1_dial.position == 85
        assert day1_dial.zero_count == 0
        day1_dial.receive_instruction("R20")
        assert day1_dial.position == 5
        assert day1_dial.zero_count == 0
        day1_dial.receive_instruction("L5")
        assert day1_dial.position == 0
        assert day1_dial.zero_count == 1
        day1_dial.receive_instruction("L2")
        assert day1_dial.position == 98
        assert day1_dial.zero_count == 1
        day1_dial.receive_instruction("R2")
        assert day1_dial.position == 0
        assert day1_dial.zero_count == 2

    def test_receive_instructions(self):
        """s"""
        instructions = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82"
        ]

        day1_dial = Day1Dial(50)
        day1_dial.receive_instructions(instructions)
        assert day1_dial.position == 32
        assert day1_dial.zero_count == 3