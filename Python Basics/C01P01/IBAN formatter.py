def iban_formatter(iban):
    concatenated_iban = ''.join(iban.split())
    final_iban = ''

    for i in range(len(concatenated_iban)):
        final_iban += concatenated_iban[i]

        if (i + 1) % 4 == 0:
            final_iban += ' '

    return final_iban


tests = [
    ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54")
]

for iban, expected_iban in tests:
    if expected_iban == iban_formatter(iban):
        print(True)
    else:
        print(False)
