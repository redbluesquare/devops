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

print(calc( sys.argv[1], sys.argv[2], sys.argv[3]))