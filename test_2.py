import pytest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CSV file setup
def log_test_result(test_name, status, error_message=""):
    with open("test_results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([test_name, status, error_message])

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000")
    driver.implicitly_wait(5)  # Set implicit wait
    with open("test_results.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Name", "Status", "Error Message"])
    yield driver
    driver.quit()

@pytest.mark.parametrize("xpath", [
    ('/html/body/div/div[2]/div[1]/a'),
    ('//*[@id="grid-state"]'),
    ('//*[@id="test"]/form/button'),
    ('/html/body/div/div[1]/ul/li[1]/a'),
    ('/html/body/div/div[1]/ul/li[2]/a'),
    ('/html/body/div/div[1]/ul/li[3]/a'),
])
def test_click_elements(driver, xpath):
    test_name = f"Click Test {xpath}"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        log_test_result(test_name, "Passed")
    except Exception as e:
        log_test_result(test_name, "Failed", str(e))
        pytest.fail(f"Element {xpath} not found or not clickable: {e}")

@pytest.mark.parametrize("input_xpath, value", [
    ('//*[@id="grid-first-name"]', '6'),
    ('//*[@id="grid-last-name"]', '7'),
    ('/html/body/div/div[2]/div[2]/form/div[3]/div[1]/input', '7'),
    ('/html/body/div/div[2]/div[2]/form/div[3]/div[2]/input', '8'),
    ('/html/body/div/div[2]/div[2]/form/div[4]/div[1]/input', '7'),
    ('/html/body/div/div[2]/div[2]/form/div[4]/div[2]/input', '25')
])
def test_input_fields(driver, input_xpath, value):
    test_name = f"Input Test {input_xpath}"
    try:
        field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        field.clear()
        field.send_keys(value)
        assert field.get_attribute("value") == value, f"Value not entered correctly in {input_xpath}"
        log_test_result(test_name, "Passed")
    except Exception as e:
        log_test_result(test_name, "Failed", str(e))
        pytest.fail(f"Input field {input_xpath} not found or not interactable: {e}")

def test_text_extraction(driver):
    test_name = "Text Extraction Test"
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/p[3]'))
        )
        text = element.text
        assert text.strip() != "", "Extracted text is empty"
        log_test_result(test_name, "Passed")
    except Exception as e:
        log_test_result(test_name, "Failed", str(e))
        pytest.fail(f"Text extraction failed: {e}")