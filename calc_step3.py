import sys
import math
def calc( operator, number_1, number_2):
    if operator == '+':
        try:
            answer = float(number_1) + float(number_2)
        except Exception as e:
            answer = str(e)
        finally:
            return answer
    elif operator == '-':
        try:
            answer = float(number_1) - float(number_2)
        except Exception as e:
            answer = str(e)
        finally:
            return answer
    elif operator == 'x':
        try:
            answer = float(number_1) * float(number_2)
        except Exception as e:
            answer = str(e)
        finally:
            return answer
    elif operator == '/':
        try:
            answer = float(number_1) / float(number_2)
        except Exception as e:
            answer = str(e)
        finally:
            return answer
    else:
        return "operator incorrect"
    print(answer)

with open('step_3.txt', 'r') as txt_file:
    contents = txt_file.readlines()
goto = 0
statements = []
check = False
while check == False:
    line = contents[goto]
    row = line.strip().split(" ")
    if row[1] == 'calc':
        if line in statements:
            print(line)
            print(goto+1)
            check = True
        else:
            statements.append(line)
    else:
        if line in statements:
            print(line)
            print(goto+1)
            check = True
        else:
            statements.append(line)
# print(goto)
# print(calc( sys.argv[1], sys.argv[2], sys.argv[3]))