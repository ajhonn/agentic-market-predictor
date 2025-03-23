def inc(x: int) -> int:
    return x + 1


def test_answer() -> None:
    test_ans = 5
    if inc(3) != test_ans:
        err_message = "Expected same value;"
        raise ValueError(err_message)
