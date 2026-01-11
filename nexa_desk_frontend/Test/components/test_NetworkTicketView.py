from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5173"
USER_EMAIL = "userEmir@sen4015.com"   
USER_PASSWORD = "123"                 


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    wait = WebDriverWait(driver, 10)
    test_passed = False 

    try:
       
        driver.get(BASE_URL)

        
        email_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(USER_EMAIL)

        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.clear()
        password_input.send_keys(USER_PASSWORD)

        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Sign in')]")
            )
        )
        sign_in_button.click()

        
        wait.until(EC.url_contains("/dashboard"))

        dashboard_heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )
        assert "IT Support Dashboard" in dashboard_heading.text
        print("Login successful, dashboard opened")

        
        network_link = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'View network tickets')]"
                " | //a[contains(., 'View network tickets')]"
            ))
        )
        network_link.click()

        
        network_heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h1[normalize-space()='Network Tickets']"
                " | //h2[normalize-space()='Network Tickets']"
            ))
        )

        assert "Network Tickets" in network_heading.text
        print("Network Tickets page opened")

        test_passed = True  

    except Exception as e:
        import traceback
        print("Test FAILED:", type(e).__name__)
        traceback.print_exc()

    finally:
        driver.quit()

        if test_passed:
            print("TEST RESULT: PASSED")
        else:
            print("TEST RESULT: FAILED")


if __name__ == "__main__":
    main()
