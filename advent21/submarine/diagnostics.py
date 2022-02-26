def _most_common_digits(nums):
    digits = [[0, 0] for i in range(len(nums[0]))]

    for num in nums:
        for i, digit in enumerate(num):
            if digit == '0':
                digits[i][0] += 1
            elif digit == '1':
                digits[i][1] += 1
            else:
                raise RuntimeError(f'Digit {digit} must be binary')

    result = ''

    for zero, one in digits:
        if zero > one:
            result += '0'
        else:
            result += '1'

    return result


def get_rates(report):
    gamma = _most_common_digits(report)

    epsilon = ''
    for digit in gamma:
        epsilon += '0' if digit == '1' else '1'

    return int(gamma, 2), int(epsilon, 2)


class _BitCriteria:
    def __call__(self, num):
        raise NotImplementedError


class _OxygenGeneratorCriteria(_BitCriteria):
    def __init__(self, nums, pos):
        self.__most_common = _most_common_digits(nums)
        self.__pos = pos

    def __call__(self, num):
        return num[self.__pos] == self.__most_common[self.__pos]


class _C02ScrubberCriteria(_BitCriteria):
    def __init__(self, nums, pos):
        self.__most_common = _most_common_digits(nums)
        self.__pos = pos

    def __call__(self, num):
        return num[self.__pos] != self.__most_common[self.__pos]


def _find_num(report, criteria_type):
    nums = report

    for i in range(len(nums[0])):
        criteria = criteria_type(nums, i)
        next_nums = []

        for num in nums:
            if criteria(num):
                next_nums.append(num)

        if len(next_nums) == 1:
            return next_nums[0]

        nums = next_nums

    assert False


def oxygen_generator_rating(report):
    return int(_find_num(report, _OxygenGeneratorCriteria), 2)


def c02_scrubber_rating(report):
    return int(_find_num(report, _C02ScrubberCriteria), 2)


def life_support_rating(report):
    return oxygen_generator_rating(report) * c02_scrubber_rating(report)


def power_consumption(report):
    gamma, epsilon = get_rates(report)
    return gamma * epsilon
