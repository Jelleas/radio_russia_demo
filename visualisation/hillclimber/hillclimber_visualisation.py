import matplotlib.pyplot as plt
import csv

__all__ = [
    "hillclimb_graph",
    "hillclimber_averages_graph",
    "hillclimber_averages_filled_graph",
    "hillclimber_xopt_comparison_graph",
]


def hillclimb_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climber')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/hillclimber/single_run.png")


def hillclimber_averages_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='HillClimber')
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages.png")


def hillclimber_averages_filled_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/hillclimber/hillclimber_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [(float(average), int(minimum), int(maximum)) for average, minimum, maximum in result_reader]
        averages = [average for average, minimum, maximum in results]
        minima = [minimum for average, minimum, maximum in results]
        maxima = [maximum for average, minimum, maximum in results]

    ax.plot(averages, label='HillClimber')
    ax.fill_between(range(0, len(averages)), minima, maxima, alpha=0.5, linewidth=0)
    ax.set_title('Hill Climbers (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/hillclimber/hillclimber_averages_filled.png")


def hillclimber_xopt_comparison_graph() -> None:
    fig, ax = plt.subplots()
    results = []
    for n in range(1, 6):
        with open(f"results/hillclimber/hillclimber_xopt_{n}.csv", 'r') as input_file:
            result_reader = csv.reader(input_file, delimiter=',')
            results.append([float(value) for value, _, _ in result_reader])

    for index, result in enumerate(results):
        ax.plot(result, label=f'X-Opt {index + 1}')

    ax.legend(loc='upper right')
    ax.set_title('Hill Climber X-Opts (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/hillclimber/hillclimber_xopt_comparison.png")
