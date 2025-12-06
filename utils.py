"""a"""
def get_input (filename):
    """e.g. input/day1.txt"""
    with open(f"input/{filename}") as f:
        text = f.read()

    return text.splitlines()
