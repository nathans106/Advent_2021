class Card:
    def __init__(self, nums):
        self.__routes = []
        length = len(nums[0])

        for i, row in enumerate(nums):
            self.__routes.append({num for num in row})
            self.__routes.append({nums[c][i] for c in range(length)})

    def call(self, num):
        if self.__cross_nums(num):
            return self.__calculate_score(num)

        return None

    def __cross_nums(self, num):
        success = False

        for route in self.__routes:
            if num in route:
                route.remove(num)

            if len(route) == 0:
                success = True

        return success

    def __calculate_score(self, num):
        uniques = set()
        for route in self.__routes:
            uniques = uniques.union(route)

        return sum(uniques) * num


def winning_score(cards, calls):
    for call in calls:
        high_score = 0

        for card in cards:
            score = card.call(call)
            if score and score > high_score:
                high_score = score

        if high_score > 0:
            return high_score

    raise RuntimeError('No cards succeeded')


def last_score(cards, calls):
    remaining = cards
    for call in calls:
        to_remove = []
        for card in remaining:
            score = card.call(call)
            if score:
                if len(remaining) == 1:
                    return score
                else:
                    to_remove.append(card)

        for card in to_remove:
            remaining.remove(card)

    raise RuntimeError('Multiple scores were last')

def parse_card(lines):
    nums = []

    for line in lines:
        nums.append([int(num) for num in line.split(' ')])

    return Card(nums)
