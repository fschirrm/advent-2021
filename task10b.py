import utils.utils as utils


def closing_value(closing_char):
    if closing_char == ")":
        return 1
    if closing_char == "]":
        return 2
    if closing_char == "}":
        return 3
    if closing_char == ">":
        return 4
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
points=0
for elem in c:
    inp_list.append(list(elem[0]))
correction_value_list=[]
for elem in inp_list:
    lifo = []
    correct=True
    for e1 in elem:
        if e1 in {"[", "(", "{", "<"}:
            lifo.append(e1)
        else:
            if correct_closing(lifo[-1]) == e1:
                lifo.pop(-1)
            else:
                points += closing_value(e1)
                correct=False
                break   
    if correct:
        closing_number=0
        for i in range(len(lifo)):
            closing_number = closing_number * 5 + closing_value(correct_closing(lifo[-1]))
            lifo.pop(-1)
        correction_value_list.append(closing_number)
correction_value_list.sort()
middle_score = correction_value_list[len(correction_value_list) // 2]
print(f"Middle Score = {middle_score}")
