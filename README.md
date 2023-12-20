# Advent Of Code

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.

## Running

Each challange should have it's only individual readme. With each challange being placed in a `./Challanges/<Year>/Day <day>` folder.

## Setup

Activate your shell

```sh
./Scripts/activate
```

Install Requirements

```sh
pip install -r requirements.txt
```

# Updating 

Ensure you're running in the virtual environment to make sure just the projects requirements are updated

```sh
./Scripts/activate
```

Include any updates to the libraries made

```sh
pip freeze > requirements.txt
```

# Set up Of venv

```sh
python -m venv .
```