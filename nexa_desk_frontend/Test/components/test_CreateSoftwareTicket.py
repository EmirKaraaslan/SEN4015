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

    test_passed = False  # Test result flag

    test_title = "Selenium test ticket"
    test_description = "Can not connect power platform"
    test_priority = "Medium"

    try:
        # =======================
        # 1) LOGIN
        # =======================
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

        # =======================
        # 2) SOFTWARE TICKETS PAGE
        # =======================
        wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'View software tickets')] | "
                "//a[contains(., 'View software tickets')]"
            ))
        ).click()

        software_heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h1[normalize-space()='Software Tickets'] | "
                "//h2[normalize-space()='Software Tickets']"
            ))
        )
        assert "Software Tickets" in software_heading.text
        print("Software Tickets page opened")

        # =======================
        # 3) OPEN CREATE TICKET FORM
        # =======================
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Create ticket')]")
            )
        ).click()

        # =======================
        # 4) FILL THE FORM
        # =======================
        wait.until(
            EC.visibility_of_element_located((By.ID, "title"))
        ).send_keys(test_title)

        wait.until(
            EC.visibility_of_element_located((By.ID, "description"))
        ).send_keys(test_description)

        Select(
            wait.until(EC.element_to_be_clickable((By.ID, "priority")))
        ).select_by_visible_text(test_priority)

        # =======================
        # 5) SUBMIT (CREATE)
        # =======================
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Create']")
            )
        ).click()

        # =======================
        # 6) VERIFY TABLE ROW
        # =======================
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

        id_el = new_row.find_element(By.XPATH, ".//span[1]")
        title_el = new_row.find_element(By.XPATH, ".//span[2]")
        category_el = new_row.find_element(By.XPATH, ".//span[3]")
        priority_el = new_row.find_element(By.XPATH, ".//span[4]//span")
        status_el = new_row.find_element(By.XPATH, ".//span[5]//span")
        updated_el = new_row.find_element(By.XPATH, ".//span[6]")

        print(
            "New row:",
            id_el.text.strip(),
            title_el.text.strip(),
            category_el.text.strip(),
            priority_el.text.strip(),
            status_el.text.strip(),
            updated_el.text.strip(),
        )

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
