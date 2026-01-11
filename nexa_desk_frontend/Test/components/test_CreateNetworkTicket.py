from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    test_passed = False  #

    test_title = "Selenium test ticket"
    test_description = "Laptop is not working properly."
    test_priority = "Medium"

    try:
        
       
        
        driver.get(BASE_URL)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys(USER_EMAIL)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        ).send_keys(USER_PASSWORD)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign in')]"))
        ).click()

        wait.until(EC.url_contains("/dashboard"))

        dashboard_heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )
        assert "IT Support Dashboard" in dashboard_heading.text
        print("Login successful, dashboard opened")


        wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'View network tickets')] | "
                "//a[contains(., 'View network tickets')]"
            ))
        ).click()

        network_heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h1[normalize-space()='Network Tickets'] | "
                "//h2[normalize-space()='Network Tickets']"
            ))
        )
        assert "Network Tickets" in network_heading.text
        print("Network Tickets page opened")

  
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Create ticket')]")
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "title"))
        ).send_keys(test_title)

        wait.until(
            EC.visibility_of_element_located((By.ID, "description"))
        ).send_keys(test_description)

        Select(
            wait.until(EC.element_to_be_clickable((By.ID, "priority")))
        ).select_by_visible_text(test_priority)


        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Create']")
            )
        ).click()


        new_row = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                (
                    "//div[contains(@class, 'tickets-list__row')]["
                    ".//span[contains(@class,'tickets-list__cell--title') "
                    f"and normalize-space()='{test_title}']]"
                )
            ))
        )

        title_el = new_row.find_element(By.XPATH, ".//span[2]")
        assert title_el.text.strip() == test_title

        print("Ticket creation test PASSED")
        test_passed = True  # Test passed

    except Exception as e:
        import traceback
        print("Test FAILED:", type(e).__name__)
        traceback.print_exc()

    finally:
        if not test_passed:
            input("Test failed - press Enter to close the browser...")
        driver.quit()


if __name__ == "__main__":
    main()
