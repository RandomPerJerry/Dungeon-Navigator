import configs
import random

def generate_unique_positions(static_saw, moving_saws):
    # static_saw: int, moving_saws: int
    global static_saw_cord

    assert static_saw + moving_saws > 0, "Invalid number of saws. Must be greater than 0."

    static_saw_cord = []
    moving_saws_cord = []

    target_range = ((100, 200), (configs.SCREEN_DIMENTION[0] - 100, configs.SCREEN_DIMENTION[1] - 200))

    total_saws = static_saw + moving_saws

    # Calculate the dimensions of the smaller rectangles
    width = (target_range[1][0] - target_range[0][0]) // total_saws
    height = (target_range[1][1] - target_range[0][1]) // total_saws

    rect_list = []
    for i in range(target_range[0][0], target_range[1][0], width):
        for j in range(target_range[0][1], target_range[1][1], height):
            rect_list.append(((i, j), (i + width, j + height)))

    for i in range(static_saw):
        chosen_square = random.choice(rect_list)
        chosen_cord = (random.randint(chosen_square[0][0], chosen_square[1][0]), random.randint(chosen_square[0][1], chosen_square[1][1]))
        rect_list.remove(chosen_square)
        static_saw_cord.append(chosen_cord)

    for i in range(moving_saws):
        chosen_square = random.choice(rect_list)
        chosen_cord = (random.randint(chosen_square[0][0], chosen_square[1][0]), random.randint(chosen_square[0][1], chosen_square[1][1]))
        move_range = (random.randint(100, 200), random.randint(0, 50))
        rect_list.remove(chosen_square)
        moving_saws_cord.append((chosen_cord, move_range))

        

    return static_saw_cord, moving_saws_cord

