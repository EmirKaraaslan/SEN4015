from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


BASE_URL = "http://localhost:5173"  # Frontend adresin
USER_EMAIL = "userEmir@sen4015.com"      # kendi user mailin
USER_PASSWORD = "123"       # kendi şifren


def main():
    # --- Chrome driver ayarla ---
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # CI'da koşacaksan headless açabilirsin:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 10)

    try:
        # 1) Login sayfasına git
        driver.get(BASE_URL)

        # 2) Email alanını bul ve doldur
        # React formunda "name" attribute'u email ise By.NAME ile yakalıyoruz
        email_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(USER_EMAIL)

        # 3) Password alanını bul ve doldur
        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.clear()
        password_input.send_keys(USER_PASSWORD)

        # 4) Sign in butonuna tıkla
        # Button text'i "Sign in" olduğu için XPATH ile yakalıyoruz
        sign_in_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Sign in')]")
            )
        )
        sign_in_button.click()

        # 5) Dashboard'a yönlendirme oldu mu?
        wait.until(EC.url_contains("/dashboard"))

        # 6) "IT Support Dashboard" başlığını görebiliyor muyuz?
        heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[contains(., 'IT Support Dashboard')]")
            )
        )

        assert "IT Support Dashboard" in heading.text
        print("✅ Login testi BAŞARILI: Dashboard açıldı.")

    except Exception as e:
        print("❌ Login testi HATALI:", e)

    finally:
        input("Pencereyi kapatmak için Enter'a bas...")
        driver.quit()


if __name__ == "__main__":
    main()
