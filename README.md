
# Rule Engine with Abstract Syntax Tree(AST)

### Table of contents

1.Project overview

2.Features  

3.Architecture

4.Technologies Used

5.Installation

6.Running the code

7.How the Rule Engine Works

8.Design Choices

9.Testing

10.Contributing

11.Conclusion

---

## Project Overview

The Rule Engine with AST is a 3-tier application designed to determine user eligibility based on various attributes such as age, department, income, and experience. It leverages an Abstract Syntax Tree (AST) to represent conditional rules, allowing for the dynamic creation, combination, and modification of these rules.

---
### Features

- Dynamic Rule Creation: Create rules using an abstract syntax tree structure.
- Rule Combination: Combine multiple rules into a single logical structure using AND and OR operators.

- Rule Evaluation: Evaluate a dataset against the defined rules to check if conditions are satisfied.

- Manual Condition Evaluation: Support for operators like >, <, and ==.
---
### Architecture

The application consists of the following components:

- API Layer: Handles incoming requests and routes them to the appropriate service functions.
- Service Layer: Contains the business logic for rule creation, combination, and evaluation.
- Data Layer: Manages the storage and retrieval of rules using SQLAlchemy and SQLite.
---
### Technologies Used

- Backend Framework: Fast API
- Data Structure: Abstract Syntax Tree (AST)
- Language: Python 
- In-memory Database: For storing rules during runtime (can be extended to a persistent database)
- Testing Framework: Unit test
---
### Installation
- Clone the repository to your local machine.
```
git clone https://github.com/yourusername/Rule-Engine-With-AST.git
cd rule-engine-ast
```
- Install Python

  [Download the latest version of Python](https://www.python.org/downloads/)

- Create a Virtual Environment
```
python -m venv venv
```
Activate the Virtual Environment
- For Windows
```
.\venv\Scripts\activate
```

- For Mac/Linux
```
source venv/bin/activate
```
---
### Running the Code

Run the application using the following command
```
uvicorn app.main:app --reload
```
Access the application in your web browser at:

- http://127.0.0.1:8000
- Swagger UI for API documentation at http://127.0.0.1:8000/docs

---
### How the Rule Engine Works
- Abstract Syntax Tree (AST): The rule engine uses an AST to represent rules. This allows for 
   easy manipulation, evaluation, and combination of rules.
- Creating Rules: The create_rule function takes a rule string as input and converts it into an 
AST.
- Combining Rules: The combine_rulesfunction takes multiple ASTs and combines them into 
  a single AST.
- Evaluating Rules: The evaluate_rule function takes a JSON representation of the AST and 
   user data as input, and returns True or False based on whether the user satisfies the rule.
---
### Design Choices:
##### Abstract Syntax Tree (AST)

- The application uses an AST to represent conditional rules.
- Operator Node: Represents logical operators like AND/OR.
- Operand Node: Represents conditions like age > 30 or department = 'Sales'.

##### Rule Parsing and Combination
- The create_rule function parses the rule string into tokens and builds the corresponding AST.
- The combine_rule function allows combining multiple rules into one AST using logical operators (e.g., AND, OR).

##### API Design
- Fast API was chosen for its simplicity, performance, and automatic generation of interactive documentation.
- The application includes two core endpoints: create_rule for generating ASTs and evaluate_rule for evaluating them against user data.
---
### Testing 
- Create individual rules from examples and verify their AST representation.
- Combine rules and ensure the resulting AST reflects the combined logic.
- Evaluate rules against sample JSON data to test various scenarios.
---
### Contributing

Steps to contribute:

1.Fork the repository.

2.Create a new branch.

3.Make your changes and commit them.

4.Submit a pull request for review.

---
### Conclusion

This Rule Engine application provides a flexible and efficient way to evaluate user eligibility based on dynamic rules. Future improvements could include a user interface, persistent data storage, and enhanced error handling.
