from radio_russia.algorithms import greedy as gr
import csv


def random_greedy(graph, transmitters, scheme=1, iterations=10000,
                   output_file="results/greedy/random_greedy.csv"):
    results = []
    for _ in range(iterations):
        random_greedy_graph = gr.RandomGreedy(graph, transmitters.get_scheme(scheme))
        random_greedy_graph.run()
        results.append((random_greedy_graph.graph.calculate_value(), random_greedy_graph.graph.to_json()))

    with open(output_file, 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        for result in results:
            result_writer.writerow(result)


def greedy(graph, transmitters, scheme=1, output_file="results/greedy/greedy.csv"):
    greedy_graph = gr.Greedy(graph, transmitters.get_scheme(scheme))
    greedy_graph.run()
    with open(output_file, 'w', newline='') as output_file:
        result_writer = csv.writer(output_file, delimiter=',')
        result_writer.writerow((greedy_graph.graph.calculate_value(), greedy_graph.graph.to_json()))
