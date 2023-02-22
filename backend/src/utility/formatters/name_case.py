import re


def snake_2_camel(var: str) -> str:
    return "".join(word if idx == 0 else word.capitalize() for idx, word in enumerate(var.split(sep="_")))


def snake_2_pascal(var: str) -> str:
    return "".join(word.title() for word in var.split("_"))


def any_2_snake(var: str) -> str:
    word = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", var)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", word).lower()
