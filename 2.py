import itertools
import re

def is_valid_expression(expression):
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz∨∧→¬() ')
    return all(c in valid_chars for c in expression)

def evaluate_expression(expression, values):
    for var, val in values.items():
        expression = expression.replace(var, str(val))
    
    expression = expression.replace('∧', ' and ').replace('∨', ' or ').replace('¬', ' not ').replace('→', '<=')
    
    try:
        return eval(expression)
    except Exception as e:
        return False

def generate_truth_table(expression):
    variables = list(set(re.findall(r'[A-Za-z]+', expression)))
    variables.sort()

    print("\t".join(variables) + "\tKết quả")
    
    num_variables = len(variables)
    for combo in itertools.product([True, False], repeat=num_variables):
        values = dict(zip(variables, combo))
        
        row = [("T" if values[var] else "F") for var in variables]
        
        result = evaluate_expression(expression, values)
        
        print("\t".join(row) + "\t" + ("T" if result else "F"))

def input_expression_and_generate_table():
    expression = input("Nhập biểu thức logic (ví dụ: (A ∨ ¬B) ∧ C): ")
    
    if is_valid_expression(expression):
        generate_truth_table(expression)
    else:
        print("Biểu thức không hợp lệ.")

input_expression_and_generate_table()
