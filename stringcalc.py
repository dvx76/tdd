"""String Calculator Kata"""


def add(expr: str | None = None) -> int:
    if not expr:
        return 0

    expr = expr.replace("\n", ",")
    numbers = [int(n.strip()) for n in expr.split(",")]
    return sum(numbers)
