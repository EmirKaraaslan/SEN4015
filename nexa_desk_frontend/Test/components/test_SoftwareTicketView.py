from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5173"
USER_EMAIL = "userEmir@sen4015.com"      # kendi user mailin
USER_PASSWORD = "123"       # kendi şifren


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    wait = WebDriverWait(driver, 10)

    try:
        # 1) Login sayfasına git
        driver.get(BASE_URL)

        # 2) Email & password doldur
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

        # 3) Dashboard geldi mi?
        wait.until(EC.url_contains("/dashboard"))

        dashboard_heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )
        assert "IT Support Dashboard" in dashboard_heading.text

        print("✅ Login OK, dashboard açıldı")

        # 4) software kartındaki 'View software tickets' linkine tıkla
        software_link = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(., 'View software tickets')]"
                " | //a[contains(., 'View software tickets')]"
            ))
        )
        software_link.click()

        # 5) software Tickets sayfasına geçtiğimizi doğrula
        #   a) URL kontrolü (path'in buysa)
        # wait.until(EC.url_contains("softwareTickets"))

        #   b) Başlık kontrolü (ekranda gördüğün 'software Tickets')
        software_heading = wait.until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//h1[normalize-space()='Software Tickets']"
                " | //h2[normalize-space()='Software Tickets']"
            ))
        )

        assert "Software Tickets" in software_heading.text
        print("✅ Software Tickets sayfası açıldı – test BAŞARILI")

    except Exception as e:
        import traceback
        print("❌ Test HATALI, exception tipi:", type(e).__name__)
        traceback.print_exc()
    finally:
        input("Pencereyi kapatmak için Enter'a bas...")
        driver.quit()


if __name__ == "__main__":
    main()
