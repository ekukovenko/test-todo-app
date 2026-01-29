def divide(a: float, b: float) -> float | None:
    """
    Делит первое число на второе.

    Args:
        a: Делимое.
        b: Делитель.

    Returns:
        Результат деления или None, если происходит деление на ноль.
    """
    if b == 0:
        return None
    return a / b
