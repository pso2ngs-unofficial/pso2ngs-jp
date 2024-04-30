def is_matched_rgb(rgb: tuple, lower_limit: tuple, upper_limit: tuple) -> bool:
    return all([lower_limit[i] <= rgb[i] <= upper_limit[i] for i in range(3)])

def is_urgent_quest(pixel: tuple) -> bool:
    return is_matched_rgb(pixel, (190, 60, 60), (255, 105, 105))

def is_stage_live(pixel: tuple) -> bool:
    return is_matched_rgb(pixel, (254, 99, 254), (255, 101, 255))
