#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_show(func):
    def wrapper(width, height):
        res = func(width, height)
        print(f"Площадь прямоугольника: {res}")
        return res
    return wrapper


@func_show
def get_sq(width, height):
    return width*height


if __name__ == '__main__':
    get_sq(width=5, height=7)