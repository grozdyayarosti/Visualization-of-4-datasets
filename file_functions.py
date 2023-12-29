import os
import pandas as pd

def get_dataset(file_name):
    path = os.path.join("datasets", file_name)
    dataset = pd.read_csv(path)
    return dataset


def parse_CSV():
    datasets = []
    files = os.listdir('datasets')

    for file in files:
        dataset = get_dataset(file)
        datasets.append(dataset)
    return datasets
