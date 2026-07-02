from radio_russia.algorithms import randomise
import copy
import csv


def baseline(graph, transmitters, scheme=1, iterations=10000,
             output_file="results/random/baseline.csv"):
    results = []
    for _ in range(iterations):
        random_graph = randomise.random_reassignment(copy.deepcopy(graph), transmitters.get_scheme(scheme))
        results.append((random_graph.calculate_value(), random_graph.to_json()))

    with open(output_file, 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for result in results:
            result_writer.writerow(result)
