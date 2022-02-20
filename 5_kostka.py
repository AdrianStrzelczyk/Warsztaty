import random

DICES = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def roll_the_dice(dice_code):
    for dice in DICES:
        if dice in dice_code:
            try:
                throw, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        throw = int(throw) if throw else 1
    except ValueError:
        return "Wrong Input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(throw)]) + modifier


print(roll_the_dice("2D10+10"))
print(roll_the_dice("D6"))
print(roll_the_dice("2D3"))
print(roll_the_dice("D12-1"))
print(roll_the_dice("DD34"))
