import matplotlib.pyplot as plt
import json


def depth_first_memory_graph() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)

    ax.set_title('Depth First Memory Growth')

    ax.plot(result['states_sizes'], label='States')
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')
    fig.savefig("results/depth_first/depth_first_memory.png")


def depth_first_table() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        result = json.load(input_file)

    cells = [str(result['visited_state_count']), str(result['max_states_size']), str(result['solution_count']), str(result['value'])]

    ax.set_title('Depth First Overview')
    ax.set_axis_off()

    ax.table(
        colLabels=['Visited State Count', 'Max States Size', 'Solution Count', 'Objective Value'],
        rowLabels=["DepthFirst"],
        cellText=[cells],
        loc='upper left',
    )
    fig.tight_layout()
    fig.savefig("results/depth_first/depth_first.png")


def depth_first_memory_comparison() -> None:
    fig, ax = plt.subplots(figsize=(8, 4))
    with open("results/depth_first/depth_first.json", 'r') as input_file:
        depth_result = json.load(input_file)

    with open("results/depth_first/branchandbound.json", 'r') as input_file:
        bnb_result = json.load(input_file)

    ax.set_title('Depth First Memory Comparison')

    ax.plot(bnb_result['states_sizes'], label='BranchAndBound')
    ax.plot(depth_result['states_sizes'], label='DepthFirst')
    ax.legend(loc='upper right')

    ax.yaxis.get_major_locator().set_params(nbins=20, steps=[1, 2, 5, 10])  # type: ignore[call-arg]
    ax.set_xlabel('Considered States')
    ax.set_ylabel('Number of States')
    fig.savefig("results/depth_first/depth_first_memory_comparison.png")
