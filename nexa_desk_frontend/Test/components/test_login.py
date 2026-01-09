from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5173"   # Frontend URL
USER_EMAIL = "userEmir@sen4015.com"  # User email
USER_PASSWORD = "123"                # User password


def main():
    # --- Configure Chrome driver ---
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # For CI usage, you can enable headless mode:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 10)
    test_passed = False  # Test result flag

    try:
        # 1) Navigate to login page
        driver.get(BASE_URL)

        # 2) Locate and fill email field
        email_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(USER_EMAIL)

        # 3) Locate and fill password field
        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.clear()
        password_input.send_keys(USER_PASSWORD)

        # 4) Click the Sign in button
        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Sign in')]")
            )
        )
        sign_in_button.click()

        # 5) Verify redirection to dashboard
        wait.until(EC.url_contains("/dashboard"))

        # 6) Verify dashboard heading is visible
        heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )

        assert "IT Support Dashboard" in heading.text
        print("Login test PASSED: Dashboard is visible")

        test_passed = True

    except Exception as e:
        import traceback
        print("Login test FAILED:", type(e).__name__)
        traceback.print_exc()

    finally:
        driver.quit()

        if test_passed:
            print("TEST RESULT: PASSED")
        else:
            print("TEST RESULT: FAILED")


if __name__ == "__main__":
    main()
