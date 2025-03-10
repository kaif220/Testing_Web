# Testing_Web
# Pytest Selenium Automation with CSV Logging

Overview
This project automates testing of a local web application (`http://127.0.0.1:5000`) using Selenium WebDriver and Pytest. It includes test cases for clicking elements, filling input fields, and extracting text. Test results are logged into a CSV file (`test_results.csv`).

This automation is implemented to test a **Personality Prediction Website**, ensuring its elements and input fields function correctly.

Requirements
- Python 3.x
- Selenium
- Pytest
- Google Chrome
- ChromeDriver

Installation
1. Install the required Python packages:
   ```bash
   pip install selenium pytest
   ```
2. Download and set up [ChromeDriver](https://sites.google.com/chromium.org/driver/).

How It Works
1. **Test Setup**: 
   - A Selenium WebDriver instance is created using a pytest fixture.
   - The script waits for elements to be interactable before performing actions.
   - Test results are logged in `test_results.csv`.

2. **Test Cases:**
   - **Click Elements**: Tests navigation by clicking links and buttons.
   - **Input Fields**: Tests form input functionality.
   - **Text Extraction**: Verifies text content is present.

3. **Logging Mechanism:**
   - A `log_test_result()` function appends test results (`Passed/Failed`) with error messages (if any) into `test_results.csv`.

Running the Tests
Execute the test suite using:
```bash
pytest -v test_script.py
```
CSV Output Format
Each test result is stored in `test_results.csv` with the following structure:
```
Test Name, Status, Error Message
Click Test /html/body/div/div[2]/div[1]/a, Passed, 
Input Test //*[@id="grid-first-name"], Failed, Element not found
Text Extraction Test, Passed, 
```

## Notes
- Ensure the local web application (`http://127.0.0.1:5000`) is running before executing tests.
- This script is specifically designed for testing the **Personality Prediction Website** and may require updates if the webpage structure changes.
- Adjust XPaths if the webpage structure changes.

## License
This project is open-source and free to use.
