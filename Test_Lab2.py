import Lab2


def test_calc_average_temperature():
    input_arr = [1,2,3]
    answer = 2
    result = Lab2.calc_average_temperature(input_arr)
    assert (answer == result)


def test_calc_min_max_temperature():
    input_arr = [1, 2, 3]
    answer = (3,1)
    result = Lab2.calc_min_max_temperature(input_arr)
    assert (answer == result)


def test_calc_median_temperature():
    input_arr = [1,2,3]
    answer = 2
    result = Lab2.calc_median_temperature(input_arr)
    assert (answer == result)