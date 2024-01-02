import os, sys

input_text = "puzzle_masses_1.txt"

def get_fuel(mass):
    return (int(mass)//3)-2

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
    masses = get_file(path, input_text)

    total_fuel_requirement = 0
    for mass in masses.strip().split("\n"):
        total_fuel_requirement += get_fuel(mass)

    print(f"Total fuel requirement is {total_fuel_requirement}.")

    total_fuel_requirement = 0
    for mass in masses.strip().split("\n"):
        
        fuel = get_fuel(mass)
        print(mass, fuel)
        total_fuel_requirement += fuel
        while fuel > 0:
            fuel = get_fuel(fuel)
            print("Extra fuel ", fuel)
            if fuel > 0:
                total_fuel_requirement += fuel        
    
    print(f"Total fuel requirement for mass and fuel is is {total_fuel_requirement}.")