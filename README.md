# Simple Calculator

Objective: Develop a command-line calculator application to perform basic arithmetic operations.

Task Roadmap:

- Project Setup:
  1. Initialize a Python project and set up a virtual environment. -Done
- Development:
  1. Implement functions for addition, subtraction, multiplication, and division. -Done
  2. Use a loop to allow continuous calculations until the user decides to exit. -Done
  3. Handle invalid input and division by zero errors. -Done
- Testing:
  1. Test the calculator with various inputs to ensure accuracy. -Done
- Documentation:
  1. Provide a usage guide and example inputs. -Done
- Deployment:
  1. Make a simple UI using flask or gradio. -Done

### Author: Lucky Ali

## Steps to Run

- Clone this repository:

```bash
    git clone https://github.com/iamluckycheema/EcodeCamp_Task_Number_One.git
```

### Method 1: Command Line Interface

Performs basic 2 number calculations

- Run:

```bash
    python calculator.py
```

- Enter a number from 1-4 to perform your desired operations
- Enter first number
- Enter second number
- See results
- Choose 5 to exit

### Method 2 - Flask Based Graphical User Interface

Supports longer expressions like 2+3 or 3-0+6 or 3+(2*4)*9

- Create virtual enviournment (recommended):

```bash
  python -m venv venv
```

- Activate virtual enviournment:
- Linux/Mac:

```bash
  source venv/bin/activate
```

- Windows:

```bash
  venv\Scripts\activate
```

- Install required packages:

```bash
  pip install -r requirements.txt
```

- Run:

```bash
  python app.py
```

- Open your browser and navigate to <http://127.0.0.1:5000/>
- Use keyboad inputs (will accept only numbers or operators, 'c' of clear, 'enter' to calculate)
  OR
- Use on-screen buttons

## Testing (pytest required)

- Install pytest
- Run tests:

```bash
  pytest
```
