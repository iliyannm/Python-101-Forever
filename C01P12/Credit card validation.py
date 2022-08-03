def is_credit_card_valid(number):
    number = str(number)
    final_sum = 0
    counter = 0

    for i in range(len(number)-1, -1, -1):
        counter += 1
        current_num = int(number[i])

        if counter % 2 == 0:
            current_num *= 2
            if current_num >= 10:
                current_num = str(current_num)
                current_num = int(current_num[0]) + int(current_num[1])

        final_sum += current_num

    if final_sum % 10 == 0:
        return True
    else:
        return False


tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]

for num, answer in tests:
    if answer == is_credit_card_valid(num):
        print(True)
    else:
        print(False)
