"""
s = "abeehhhhhccced"
print(s + " => " + func(s))
s = "aaabbceedd"
print(s + " => " + func(s))
s = "abcde"
print(s + " => " + func(s))
s = "aaabbdefffff"
print(s + " => " + func(s))

Answer:
cccbba  => c3b2a
abeehhhhhccced => abe2h5c3ed
aaabbceedd => a3b2ce2d2
abcde => abcde
aaabbdefffff => a3b2def5
"""
import pytest


@pytest.mark.parametrize("input_data, expected",
                         [
                             ("cccbba", "c3b2a"),
                             ("abeehhhhhccced", "abe2h5c3ed"),
                             ("aaabbceedd", "a3b2ce2d2"),
                             ("abcde", "abcde"),
                             ("aaabbdefffff", "a3b2def5")
                         ],
                         ids=[
                             "cccbba => c3b2a",
                             "abeehhhhhccced => abe2h5c3ed",
                             "aaabbceedd => a3b2ce2d2",
                             "abcde => abcde",
                             "aaabbdefffff => a3b2def5"
                         ])
def test_letter_counter(input_data, expected):
    temp = []
    str_with_nums = ""
    while input_data:
        counter = 0
        letter = input_data[0]
        if len(input_data) == 1:
            temp.append((letter, str(counter + 1)))
            break
        for i in range(len(input_data)):
            if letter == input_data[i]:
                counter += 1
                continue
            else:
                break
        temp.append((letter, str(counter)))
        input_data = input_data[counter:]
    for i in temp:
        if i[1] <= '1':
            str_with_nums += "".join(i[0])
        else:
            str_with_nums += "".join(i)
    assert str_with_nums == expected
