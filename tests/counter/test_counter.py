from src.pre_built.counter import count_ocurrences


def test_counter():
    word_counter = count_ocurrences("data/jobs.csv", "Developer")
    assert word_counter == 352


#
