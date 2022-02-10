"""
This program takes a list of values and a desired number and finds the smallest sum

arguments: 
    file_path_to_values: a file path that contains a list of numbers in a csv file.
    desired_number: integer

usage: 
    ./find_pair.py ./data/dataTen.csv 1234
"""

import csv
import sys


def validate_list_element(x):
    #TODO: get specific exception types and combine into one try block.
    try:
        x = int(x)
    except:
        raise Exception("Data must be an integer.")

    if x > 0:
        return x
    else:
        raise Exception("All numbers must be larger than 0")


def ingest_data(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        raw_data = [] 
        for row in reader:
            raw_data.extend(row)
        
    try:
        numeric_data = list(map(validate_list_element, raw_data))
    except:
        raise 

    #possibly look for a better way to get unique values
    set_numeric_data = set(numeric_data)
    if len(numeric_data) != len(set_numeric_data):
        raise Exception("Data must be unique")
    
    #sorting data makes problem much easier to work with.
    numeric_data.sort()
    return numeric_data


def pass_edge_cases(values, desired_number):
    # values at least needs two numbers
    if len(values) < 2:
        return False

    # check if desired number is below lowest
    if values[0] > desired_number:
        return False
    
    # check if desired number is above top two 
    if values[-1] + values[-2] < desired_number:
        return False
    
    return True


def format_solution(solution):
    if solution[0] < solution[1]:
        return solution
    else:
        return [solution[1], solution[0]]


def compute_best_solution(solutions):
    if len(solutions) < 1:
        return False

    best_solution = solutions[0]
    for pair in solutions:
        pair_sum = pair[0] + pair[1]
        best_solution_sum = best_solution[0] + best_solution[1]

        if pair_sum < best_solution_sum:
            best_solution = pair
        elif pair_sum == best_solution_sum:
            if min(pair) < min(best_solution):
                best_solution = pair

    return format_solution(best_solution)


def find_pair(values, desired_number):

    if not pass_edge_cases(values, desired_number):
        return None

    solutions = []
    best_solution = [values[-1] * 2,values[-1] * 2]
    for i in range(len(values)):
        #TODO: Add an index(or separate index array) to values to start checking at better locations. 
        # Ex. if i is 1 and desired output is 12345, I don't need to check 10, 15, 23 etc. I would want to jump 
        # to somewhere in the ten thousands.
        for j in range(i+1, len(values)):
            sum = values[i] + values[j]
            if sum > desired_number or sum > best_solution[0] + best_solution[1]:
                break

            if sum == desired_number:
                solutions.append([values[i],values[j]])
         
        found_best_solution = compute_best_solution(solutions)
        if found_best_solution:
            best_solution = found_best_solution
            solutions = [best_solution]

    if best_solution[0] != values[-1]*2:
        return best_solution
    else:
        return None


def main(data_file_path, desired_number):
    #TODO: get specific exception types and combine into one try block.
    try:
        values = ingest_data(data_file_path)
    except Exception as e:
        sys.exit('Error from list of values: '+ str(e))

    try:
        desired_number = int(desired_number)
    except Exception as e:
        sys.exit('Error from desired output: '+ str(e))

    solution = find_pair(values, desired_number)

    if solution == None:
        print('No solution.')
    else:
        print("Best Solution: ", solution)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])


'''
#First thought of how to improve run time
def find_pair_solution2(values, desired_number):

    if not pass_edge_cases(values, desired_number):
        return None

    solutions = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            if i == j:
                continue

            if values[i] + values[j] == desired_number:
                solutions.append([values[i],values[j]])

    return solutions


# First quick and dirty solution
def find_pair(values, desired_number):

    solutions = []
    for i in range(len(values)):
        for j in range(len(values)):
            if i == j:
                continue

            if values[i] + values[j] == desired_number:
                solutions.append([values[i],values[j]])

    return solutions
'''