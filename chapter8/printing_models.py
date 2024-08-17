import os
from typing import List

os.system("clear")

def print_models(unprinted_designes: List[str]) -> List[str]:
    completed_models = []
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)
    return completed_models

def show_complited_models(completed_models: List[str]) -> None:
    print("\nWydrukowane zostały następujące modele: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designes = ['etui telefonu', 'robot pendant', 'dwunastościan', 'origami']

print(unprinted_designes)

completed_models = print_models(unprinted_designes)
show_complited_models(completed_models)

print(unprinted_designes)
