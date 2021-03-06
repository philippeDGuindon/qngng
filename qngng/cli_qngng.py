import argparse
import json
import operator
import os
import random
import sys
import unicodedata
from typing import Optional

import qngng
from qngng import common


def _parse_args():
    parser = argparse.ArgumentParser(description=qngng.__description__)

    parser.add_argument('--gender', '-g', choices=['male', 'female'],
                        help='Filter first names by gender')
    parser.add_argument('--snake-case', '-s', action='store_true',
                        help='Print names in "snake_case" format')
    parser.add_argument('--kebab-case', '-k', action='store_true',
                        help='Print names in "kebab-case" format')
    parser.add_argument('--weighted', '-w', action='store_true',
                        help='Pick names according to their relative popularity')
    parser.add_argument('--doublename', '-d', action='store_true',
                        help='Create a double-barrelled name')
    args = parser.parse_args()
    common._validate_snake_kebab_args(args)
    return args


def _read_name_file(filename):
    file_path = os.path.join(common._DATA_DIR, filename)
    with open(file_path) as f:
        names = json.load(f)

    return names


def _get_names(gender: Optional[str] = None):
    names = _read_name_file('names.json')

    if gender:
        names = [name for name in names if name['gender'] == gender]

    return names


def _get_surnames():
    return _read_name_file('surnames.json')


def _get_random_name(name_list) -> str:
    length = len(name_list)
    index = random.randrange(length)

    return name_list[index]['name']


def _get_weighted_random_name(name_list) -> str:
    name_list = sorted(
        name_list,
        key=operator.itemgetter('weight'),
        reverse=True,
    )

    total_weight = sum(entry['weight'] for entry in name_list)
    random_weight = random.randrange(total_weight + 1)

    for entry in name_list:
        random_weight -= entry['weight']
        if random_weight <= 0:
            return entry['name']


def _run(args):
    names = _get_names(gender=args.gender)
    surnames = _get_surnames()

    if args.weighted:
        get_random_name = _get_weighted_random_name
    else:
        get_random_name = _get_random_name

    name = get_random_name(names)

    surname = get_random_name(surnames)

    if args.doublename :
        second_surname = get_random_name(surnames)
        surname = f'{surname}-{second_surname}'

    common._print_name(name, surname, args)


def main():
    args = _parse_args()

    try:
        _run(args)
    except KeyboardInterrupt:
        sys.exit(1)
