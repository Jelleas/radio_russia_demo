"""Reproduce an experiment from its JSON configuration file.

Usage:
    python -m radio_russia.run_experiment experiments/depth_first/depth_first_experiment.json
"""
import argparse
import importlib.util
import json
from pathlib import Path
from types import ModuleType

from radio_russia.classes import graph, transmitters


def load_module(json_path: Path) -> ModuleType:
    module_path = json_path.with_suffix(".py")
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_experiment(json_path: Path) -> None:
    with open(json_path, 'r') as config_file:
        config = json.load(config_file)

    data_folder = config["data_folder"]
    scheme = config.get("scheme", 1)

    test_graph = graph.Graph(f"data/{data_folder}/{data_folder}_regions.csv")
    cost_scheme = transmitters.CostScheme("data/transmitters.csv")

    module = load_module(json_path)

    for run in config["runs"]:
        function = getattr(module, run["function"])
        params = run.get("params", {})
        print(f"Running {run['function']}...")
        function(test_graph, cost_scheme, scheme=scheme, **params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path,
                         help="Path to an experiment JSON file, e.g. "
                              "experiments/depth_first/depth_first_experiment.json")
    args = parser.parse_args()

    run_experiment(args.config)
