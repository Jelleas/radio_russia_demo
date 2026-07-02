import matplotlib.pyplot as plt
import json

__all__ = [
    "breadth_first_memory_graph",
    "breadth_first_table",
    "constructive_comparison",
    "breadth_first_memory_comparison",
    "constructive_memory_comparison",
]


def breadth_first_memory_graph() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(result['states_sizes'], label='States')
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')
    fig.savefig("results/breadth_first/breadth_first_memory.png")


def breadth_first_table() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))

    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)

    cells = [str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])]

    ax.set_title('Breadth First Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst"],
        cellText=[cells],
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/breadth_first/breadth_first.png")


def constructive_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    results = []
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/depth_first/branchandbound.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    with open("results/breadth_first/best_first.json", 'r') as input_file:
        result = json.load(input_file)
        results.append([str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])])

    ax.set_title('Constructive Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst", "BranchAndBound", "BreadthFirst", "BestFirst"],
        cellText=results,
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/breadth_first/comparison.png")
    fig.savefig("results/depth_first/comparison.png")


def breadth_first_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)

    with open("results/breadth_first/best_first.json", 'r') as input_file:
        best_result = json.load(input_file)

    ax.set_title('Breadth First Memory Comparison')

    ax.plot(breadth_result['states_sizes'], label='BreadthFirst')
    ax.plot(best_result['states_sizes'], label='BestFirst')
    ax.legend(loc='upper right')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')
    fig.savefig("results/breadth_first/breadth_first_memory_comparison.png")


def constructive_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/breadth_first/breadth_first.json", 'r') as input_file:
        breadth_result = json.load(input_file)

    with open("results/depth_first/depth_first.json", 'r') as input_file:
        depth_result = json.load(input_file)

    ax.set_title('Breadth First Memory Growth')

    ax.plot(breadth_result['states_sizes'], label='States')
    ax.plot(depth_result['states_sizes'], label='States')

    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')
    fig.savefig("results/breadth_first/memory_comparison.png")
