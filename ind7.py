#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_show(func):
    def wrapper(*args, **kwargs):
        return f"Площадь прямоугольника: {func(*args, **kwargs)}"
    return wrapper


@func_show
def get_sq(width, height):
    return width*height


if __name__ == '__main__':
    print(get_sq(width=5, height=7))