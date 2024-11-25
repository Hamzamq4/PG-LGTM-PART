#!/usr/bin/env python3

import json
import sys

def main(json_file, dot_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract the data based on your CodeQL query's select statement
    # Adjust the keys based on the actual JSON structure
    edges = []
    for result in data.get('results', []):
        caller = result.get('columns', [])[1].get('value', '')
        callee = result.get('columns', [])[2].get('value', '')
        if caller and callee:
            edges.append((caller, callee))

    with open(dot_file, 'w') as f:
        f.write('digraph CallGraph {\n')
        for caller, callee in edges:
            f.write(f'  "{caller}" -> "{callee}";\n')
        f.write('}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_dot.py <input_json> <output_dot>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
