from random import randint
import uuid

e = 1


def generate_rand_point_in_rect(width, height):
    return randint(0 + e, width - e), randint(0 + e, height - e)


def gen_id() -> str:
    return uuid.uuid1().hex


def get_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
