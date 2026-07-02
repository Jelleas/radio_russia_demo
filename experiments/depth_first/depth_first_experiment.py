from radio_russia.algorithms import depth_first as df
import json

def depth_first(graph, transmitters, scheme=1, transmitter_count=4,
                 output_file="results/depth_first/depth_first.json"):
    depth = df.DepthFirst(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    depth.run()

    with open(output_file, 'w', newline='') as output_file:
        json.dump({
            'visited_state_count': depth.visited_state_count,
            'max_states_size': depth.max_states_size,
            'solution_count': depth.solution_count,
            'states_sizes': depth.states_sizes,
            'value': depth.graph.calculate_value(),
            'solution': depth.graph.to_json()
        }, output_file)

def branchandbound(graph, transmitters, scheme=1, transmitter_count=4,
                    output_file="results/depth_first/branchandbound.json"):
    depth = df.BranchAndBound(graph, transmitters.get_scheme(scheme)[0:transmitter_count])
    depth.run()

    with open(output_file, 'w', newline='') as output_file:
        json.dump({
            'visited_state_count': depth.visited_state_count,
            'max_states_size': depth.max_states_size,
            'solution_count': depth.solution_count,
            'states_sizes': depth.states_sizes,
            'value': depth.graph.calculate_value(),
            'solution': depth.graph.to_json()
        }, output_file)
