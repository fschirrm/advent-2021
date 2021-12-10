import utils.utils as utils


def closing_value(closing_char):
    if closing_char == ")":
        return 3
    if closing_char == "]":
        return 57
    if closing_char == "}":
        return 1197
    if closing_char == ">":
        return 25137
    return 0


def correct_closing(opening_char):
    if opening_char == "(":
        return ")"
    if opening_char == "[":
        return "]"
    if opening_char == "{":
        return "}"
    if opening_char == "<":
        return ">"
    return ""


c = utils.read_file("files/task10.txt")
inp_list = []
for elem in c:
    inp_list.append(list(elem[0]))
points = 0
for elem in inp_list:
    lifo = []
    for e1 in elem:
        if e1 in {"[", "(", "{", "<"}:
            lifo.append(e1)
        else:
            if correct_closing(lifo[-1]) == e1:
                lifo.pop(-1)
            else:
                points += closing_value(e1)
                break
print(points)
