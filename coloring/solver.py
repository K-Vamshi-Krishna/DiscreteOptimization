#!/usr/bin/python
# -*- coding: utf-8 -*-

from ortools.constraint_solver import pywrapcp
def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
	#print edge_count
	#for edge in edges:
	#	print edge
	
	#exit()
	
	solver = pywrapcp.Solver("coloring")
	digits = range(0,node_count)
	color =[0]* node_count
	#exit()
	for i in range(0,node_count):
		color[i] = solver.IntVar(digits,"")
	
	#solver.Add(maximum)
	for a,b in edges:
		solver.Add(color[a]!=color[b])
	
	#solver.Add(color[0] == 0)
	max_color = solver.Max(color).Var()
	maximum = solver.Minimize(max_color,1)
	solution = solver.Assignment()
	#solver.Add(max_color)
	#solver.Add(color)
	solution.Add(color)
	solution.Add(max_color)
	db = solver.Phase(color,solver.ASSIGN_CENTER_VALUE,solver.ASSIGN_MIN_VALUE)
	
	collector = solver.LastSolutionCollector(solution)
	limit = solver.TimeLimit(300)
	solver.Solve(db,[collector,maximum,limit])
	#print collector.SolutionCount()
	
	sol_color = collector.Value(0,max_color)
	#maxColor = max_color.Var()
	color_solution = [0] *node_count
	for idx in range(node_count):
		color_solution[idx] = collector.Value(0,color[idx])
    # prepare the solution in the specified output format
    output_data = str(int(sol_color + 1)) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, color_solution))
    #print "failures:", solver.Failures()
    #print "branches:", solver.Branches()
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

