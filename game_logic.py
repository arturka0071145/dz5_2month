import random

def generate_winning_slot():
    return random.randint(1, 30)


def check_win(selected_slot, winning_slot):
    return selected_slot == winning_slot
