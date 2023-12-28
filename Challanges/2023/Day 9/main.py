import os, sys

input_text_task_1 = "puzzle_inputs_1.txt"

class MirageMaintenance:
    def __init__(self, datasets) -> None:
        self.ds = datasets.strip().split("\n")
        self.measurements = []

    def load_dataset(self):
        self.datasets = [list(map(int, dataset.split())) for dataset in self.ds]

    def determine_increases(self, dataset):
        dataset.append([])
        difference_sum = 0
        for data_index in range(len(dataset[-2])-1):
            difference = dataset[-2][data_index+1] - dataset[-2][data_index]
            difference_sum += difference
            dataset[-1].append(difference)
        
        if difference_sum != 0:
            return self.determine_increases(dataset)
        
        return dataset

    def find_next_step(self):
        self.load_dataset()
        new_digit_sum = 0
        for dataset in self.datasets:
            ds = self.determine_increases([dataset])
            for ds_index in range(len(ds)-1, -1, -1):
                if ds_index == len(ds)-1:
                    ds[ds_index].append(0)
                    continue

                new_value = ds[ds_index+1][-1] + ds[ds_index][-1]
                ds[ds_index].append(new_value)

                if ds_index == 0:
                    new_digit_sum += new_value
        
        print(f"Sum of these extrapolated values is {new_digit_sum}.")

    def find_pre_step(self):
        self.load_dataset()
        new_digit_sum = 0
        for dataset in self.datasets:
            ds = self.determine_increases([dataset])

            for ds_index in range(len(ds)-1, -1, -1):
                if ds_index == len(ds)-1:
                    ds[ds_index].append(0)
                    continue

                new_value = ds[ds_index][0] - ds[ds_index+1][0]
                ds[ds_index].insert(0, new_value)

                if ds_index == 0:
                    new_digit_sum += new_value

        print(f"Sum of these extrapolated values is {new_digit_sum}.")   

def get_file(path, file):
    file = os.path.join(path, f"Task Inputs", file)

    if not os.path.exists(file):
        print(f"Invalid file supplied of {file}")
        sys.exit(1)

    with open(file, "r") as f:
        path_info = f.read()

    return path_info

if __name__ == "__main__":
    path = os.path.dirname(__file__)

    mirage_maintenance = MirageMaintenance(get_file(path, input_text_task_1))
    mirage_maintenance.find_next_step()
    mirage_maintenance.find_pre_step()
