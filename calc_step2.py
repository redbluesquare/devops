import sys
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

with open('step_2.txt', 'r') as txt_file:
    contents = txt_file.readlines()
total = 0
for line in contents:
    row = line.strip().split(" ")
    if row[0] == 'calc':
        total += calc( row[1], row[2], row[3])
print(total)
# print(calc( sys.argv[1], sys.argv[2], sys.argv[3]))