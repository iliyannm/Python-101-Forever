class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened

    def is_inside(self, value):
        after_start = False
        before_end = False

        if self.start_opened:
            after_start = value > self.start
        else:
            after_start = value >= self.start

        if self.end_opened:
            before_end = value < self.end
        else:
            before_end = value <= self.end

        return after_start and before_end

    def stringify(self):
        opening_bracket = "["
        closing_bracket = "]"

        if self.start_opened:
            opening_bracket = "("

        if self.end_opened:
            closing_bracket = ")"

        return f'{opening_bracket}{self.start}, {self.end}{closing_bracket}'


# closed_interval = Interval(1, 10)
#
# print(closed_interval.is_inside(1) is True)
# print(closed_interval.is_inside(5) is True)
# print(closed_interval.is_inside(10) is True)
#
# print(closed_interval.stringify() == "[1, 10]")
#
# opened_interval = Interval(1, 10, start_opened=True, end_opened=True)
#
# print(opened_interval.is_inside(1) is False)
# print(opened_interval.is_inside(5) is True)
# print(opened_interval.is_inside(10) is False)
#
# print(opened_interval.stringify() == "(1, 10)")
#
# half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)
#
# print(half_opened_interval.is_inside(1) is True)
# print(half_opened_interval.is_inside(5) is True)
# print(half_opened_interval.is_inside(10) is False)
#
# print(half_opened_interval.stringify() == "[1, 10)")
#
# half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)
#
# print(half_opened_interval.is_inside(1) is False)
# print(half_opened_interval.is_inside(5) is True)
# print(half_opened_interval.is_inside(10) is True)
#
# print(half_opened_interval.stringify() == "(1, 10]")
