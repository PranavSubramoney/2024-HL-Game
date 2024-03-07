import math


# calculate the umber of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Automated testing is below in the form (test_case, expected_vale)
to_test = [
    (1, 10, 5),
    (1, 20, 6),
    (1, 100, 8),
    (1, 1000, 11),
]

# run tests!
for item in to_test:
    # retrieve case and expected value
    low_num = item[0]
    high_num = item[1]
    expected = item[2]

    # get actual (ie: test ticket function)
    actual = calc_guesses(low_num, high_num)

    # compare actual and output pass / fall
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual} ❌❌❌")
