from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5173"

# Buraya kendi test kullanıcını yaz
USER_EMAIL = "user@example.com"
USER_PASSWORD = "Password123!"

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    wait = WebDriverWait(driver, 10)

    # Test datası
    test_title = "Selenium test ticket"
    test_category = "Laptop"
    test_priority = "Medium"

    try:
        # =======================
        # 1) LOGIN
        # =======================
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

        # Dashboard geldi mi?
        wait.until(EC.url_contains("/dashboard"))
        dashboard_heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )
        assert "IT Support Dashboard" in dashboard_heading.text
        print("✅ Login OK, dashboard açıldı")

        # =======================
        # 2) HARDWARE TICKETS SAYFASINA GİT
        # =======================
        hardware_link = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'View hardware tickets')]"
                " | //a[contains(., 'View hardware tickets')]"
            ))
        )
        hardware_link.click()

        hardware_heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h1[normalize-space()='Hardware Tickets']"
                " | //h2[normalize-space()='Hardware Tickets']"
            ))
        )
        assert "Hardware Tickets" in hardware_heading.text
        print("✅ Hardware Tickets sayfası açıldı")

        # =======================
        # 3) + CREATE TICKET BUTONUNA BAS
        # =======================
        create_ticket_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Create ticket')]")
            )
        )
        create_ticket_button.click()

        # =======================
        # 4) FORM ALANLARINI DOLDUR
        # =======================
        # Title
        title_input = wait.until(
            EC.visibility_of_element_located((By.ID, "title"))
        )
        title_input.clear()
        title_input.send_keys(test_title)

        # Category (select)
        category_select_el = wait.until(
            EC.element_to_be_clickable((By.ID, "category"))
        )
        Select(category_select_el).select_by_visible_text(test_category)

        # Priority (select)
        priority_select_el = wait.until(
            EC.element_to_be_clickable((By.ID, "priority"))
        )
        Select(priority_select_el).select_by_visible_text(test_priority)

        # =======================
        # 5) CREATE BUTONUNA BAS
        # =======================
        create_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Create']")
            )
        )
        create_button.click()

        # =======================
        # 6) TABLODA YENİ SATIRI DOĞRULA
        # =======================
        import time
        time.sleep(1)  # React state güncellensin diye minik buffer

        # Title'ı bizim test_title olan row'u bul
        new_row = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                (
                    "//div[contains(@class, 'tickets-list__row')]["
                    ".//span[contains(@class,'tickets-list__cell--title') "
                    f"       and normalize-space()='{test_title}']]"
                )
            ))
        )

        # Hücreleri sırasıyla al (ID, Title, Category, Priority, Status, Updated)
        id_el = new_row.find_element(By.XPATH, ".//span[1]")
        title_el = new_row.find_element(By.XPATH, ".//span[2]")
        category_el = new_row.find_element(By.XPATH, ".//span[3]")
        priority_el = new_row.find_element(By.XPATH, ".//span[4]//span")
        status_el = new_row.find_element(By.XPATH, ".//span[5]//span")
        updated_el = new_row.find_element(By.XPATH, ".//span[6]")

        row_id = id_el.text.strip()
        row_title = title_el.text.strip()
        row_category = category_el.text.strip()
        row_priority = priority_el.text.strip()
        row_status = status_el.text.strip()
        row_updated = updated_el.text.strip()

        print("Yeni satır:", row_id, row_title, row_category, row_priority, row_status, row_updated)

        # ASSERTLER
        assert row_title == test_title
        assert row_category == test_category
        assert row_priority == test_priority
        assert row_status == "Open"

        print("✅ Ticket oluşturma testi BAŞARILI (yeni satır doğru görünüyor)")

    except Exception as e:
        import traceback
        print("❌ Test HATALI, exception tipi:", type(e).__name__)
        traceback.print_exc()
    finally:
        input("Pencereyi kapatmak için Enter'a bas...")
        driver.quit()


if __name__ == "__main__":
    main()
