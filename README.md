
# Rule Engine with Abstract Syntax Tree(AST)

### Table of contents

1.Introduction

2.Features  

3.Technologies Used

4.Project Structure

5.Installation

6.Usage

7.Testing

8.Example Rule  

9.How the Rule Engine Works

8.Error Handling

9.Contributing

10.License

---

### Introduction

An Abstract Syntax Tree (AST) is a data structure that represents the structure of a computer program's source code.
It's a tree-like representation where each node represents a construct in the source code.ASTs are a fundamental part of how a compiler works.
This project is a simple Rule Engine using an Abstract Syntax Tree (AST) to dynamically create, combine, and evaluate rules based on conditions like age, salary, department, and experience.
The goal is to process and evaluate these rules against a dataset and determine if the conditions are met.
This Rule Engine supports basic logic operations (AND, OR) and conditions like >, <, and ==.

---
### Features

- Dynamic Rule Creation: Create rules using an abstract syntax tree structure.
- Rule Combination: Combine multiple rules into a single logical structure using AND and OR operators.

- Rule Evaluation: Evaluate a dataset against the defined rules to check if conditions are satisfied.

- Manual Condition Evaluation: Support for operators like >, <, and ==.

### Technologies Used

- Python 3.x

- No external dependencies are required (all libraries used are part of the standard Python library).

### Project Structure

- rule_engine.py: Contains the main logic for creating, combining, and evaluating rules.

- README.md: Contains instructions for running and testing the project.
---
### Installation
step 1: Clone the repository to your local machine.
git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast


step 2: Install Python

[Download the latest version of Python](https://www.python.org/downloads/)

- Run the installer and make sure to check the box that says "Add Python to PATH".

- After installation, verify the installation by running.This should return the version of Python installed(e.g., Python 3.x.x).

### Running the Code

Running the Rule Engine

Once Python is installed and the repository is cloned, you can run the main script:python rule_engine.py 

This will execute the main rule engine logic. If there are no external dependencies, the program will create and evaluate rules based on the data.

### Usage

In rule_engine.py, you will find the logic to create rules, combine rules, and evaluate rules.

The rule engine consists of three main components:

##### Creating a Rule:

Rules are created using the create_rule() function, which converts a rule string into an AST.
Each rule can use conditions like age > 30, salary > 50000, etc.
Example rule: "age > 30 AND salary > 50000".

##### Combining Rules:

Multiple rules can be combined using the combine_rules() function.
Rules are combined using logical operators like AND and OR.

##### Evaluating Rules:

Rules are evaluated against the dataset (user data) using the evaluate_rule() function.
The evaluation returns True if the dataset satisfies the rule, otherwise it returns False.


### Testing 

You can also run some test cases to validate that the rules are created, combined, and evaluated correctly. 

Create a separate Python file (e.g., test_rule_engine.py) with the test cases.

Run the test cases with the following command:python test_rule_engine.py 

### Example Rule

Some sample rules that can be created and evaluated:

- rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
- rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

### How the Rule Engine Works

1.Abstract Syntax Tree (AST): The rule engine uses an AST to represent rules. This allows for easy manipulation, evaluation, and combination of rules.

2.Creating Rules: The create_rule function takes a rule string as input and converts it into an AST.

3.Combining Rules: The combine_rules function takes multiple ASTs and combines them into a single AST.

4.Evaluating Rules: The evaluate_rule function takes a JSON representation of the AST and user data as input, and returns True or False based on whether the user satisfies the rule.

### Error Handling

- The system includes error handling for invalid rule strings and invalid user data.
- Invalid comparisons or missing operators will raise a ValueError.

### Contributing

Steps to contribute:

1.Fork the repository.

2.Create a new branch.

3.Make your changes and commit them.

4.Submit a pull request for review.

### License

This project is licensed under the MIT License.
