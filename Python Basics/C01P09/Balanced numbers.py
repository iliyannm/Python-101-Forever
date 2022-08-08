def is_number_balanced(number):
    number_as_a_list = list(str(abs(number)))
    left_part = 0
    right_part = 0

    if len(number_as_a_list) == 1:
        return True

    if len(number_as_a_list) % 2 != 0:
        number_as_a_list.pop(len(number_as_a_list) // 2)

    middle_num = int(len(number_as_a_list) / 2)

    for i in range(middle_num):
        left_part += int(number_as_a_list[i])

    for j in range(middle_num, len(number_as_a_list)):
        right_part += int(number_as_a_list[j])

    if left_part == right_part:
        return True
    else:
        return False


tests = [
    (9, True),
    (4518, True),
    (28471, False),
    (1238033, True),
    (413121412, False),
    (1234567654322, False),
    (1234567654321, True)
]

for number, answer in tests:
    if answer == is_number_balanced(number):
        print(True)
    else:
        print(False)