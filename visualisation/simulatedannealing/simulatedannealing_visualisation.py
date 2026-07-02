import matplotlib.pyplot as plt
import csv


def simulateannealing_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [int(value) for value, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealing')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig("results/simulatedannealing/single_run.png")


def simulatedannealing_averages_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [float(value) for value, _, _ in result_reader]

    ax.plot(results, label='SimulatedAnnealing')
    ax.set_title('Simulated Annealings (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/simulatedannealing/simulatedannealing_averages.png")


def simulatedannealing_averages_filled_graph() -> None:
    fig, ax = plt.subplots()
    with open("results/simulatedannealing/simulatedannealing_averages.csv", 'r') as input_file:
        result_reader = csv.reader(input_file, delimiter=',')
        results = [(float(average), int(minimum), int(maximum)) for average, minimum, maximum in result_reader]
        averages = [average for average, minimum, maximum in results]
        minima = [minimum for average, minimum, maximum in results]
        maxima = [maximum for average, minimum, maximum in results]

    ax.plot(averages, label='SimulatedAnnealing')
    ax.fill_between(range(0, len(averages)), minima, maxima, alpha=0.5, linewidth=0)
    ax.set_title('SimulatedAnnealing (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Average Total Costs')
    fig.savefig("results/simulatedannealing/simulatedannealing_averages_filled.png")


def simulatedannealing_temperature_comparisons_graph() -> None:
    fig, ax = plt.subplots()
    results = []
    for n in range(1, 60, 10):
        with open(f"results/simulatedannealing/simulatedannealing_temp_{n}.csv", 'r') as input_file:
            result_reader = csv.reader(input_file, delimiter=',')
            results.append([float(value) for value, _, _ in result_reader])

    for temp, result in zip(range(1, 60, 10), results):
        ax.plot(result, label=f'Temperature {temp}')

    ax.legend(loc='upper right')
    ax.set_title('Sim Annealing Temperatures (n=100)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Total Costs')
    fig.savefig(f"results/simulatedannealing/simulatedannealing_temp_{n}.png")
