"""
module
"""

class Day2idValidator:
    """
    Validates id ranges
    """
    invalid_id_count = 0
    invalid_id_list = []
    
    def __init__(self):
        pass

    def is_id_valid(self, id:str):
        """Is the first half of the id the same as the second half of the id"""

        if int(len(id)%2) == 1:
            return False
        
        id_a = "b"
        id_b = "a"

        if id_a == id_b:
            True

    def cycle_through_range(self, id_range:str):
        """Cycles through every id value between a min-max range"""
        pass

    def cycle_through_input(self, input:str):
        pass