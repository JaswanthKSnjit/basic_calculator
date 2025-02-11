# Basic Calculator
<code> </code>
## Setup Instructions

1. Clone Repo: <code> git clone git@github.com:JaswanthKSnjit/basic_calculator.git </code>
2. Navigate to project directory <code> cd basic_calculator </code>
3. Create a Python Virtual Environments <code> python -m venv venv </code>
4. Activate Python Virtual Environments <code> source venv/bin/activate </code>
5. Install dependencies <code> pip install -r requirements.txt </code>
6. Open the code in vscode <code> code .</code>
7. Run the Calculator Program <code> python calculator/calculator.py </code>
8. Here you can perform "Add, Subtract, Multiply, Divide, Check Calculation History, Check Last Calculation, Clear History, Use last result in New Calculation, Exit" all these operations
9. To test the code run <code> pytest tests/test_calculator.py </code>
10. For detailed test result run <code> pytest -v </code> 
11. To check  test coverage run <code> pytest --cov </code>

**NOTE:** The test coverage is at 51% because the testing is done only for 4 operations i.e., <code>add(), subtract(), multiple() and division().</code> For functions like <code> history, print_history(), and clear_history() </code> are not tested because they rely on user interaction and are ignored in the test suite.

**NOTE:** If you face any difficulties please contact me at <code> jk795 </code>
