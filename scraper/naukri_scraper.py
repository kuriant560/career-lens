from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraper.scraper_utils import start_driver
from scraper.skill_extractor import extract_skills
from database.db_connection import insert_job, insert_skill, link_job_skill

import time
import random


driver = start_driver()

print("Opening Naukri...")
driver.get("https://www.naukri.com/data-analyst-jobs")

time.sleep(random.uniform(4, 6))

wait = WebDriverWait(driver, 15)

try:
    jobs = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.srp-jobtuple-wrapper")
        )
    )

    total_jobs = len(jobs)
    print("Jobs found:", total_jobs)

    index = 0

    while index < total_jobs:

        try:
            # 🔥 Re-fetch elements every loop (VERY IMPORTANT)
            jobs = driver.find_elements(By.CSS_SELECTOR, "div.srp-jobtuple-wrapper")
            job = jobs[index]

            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(random.uniform(1, 2))

            title_elem = job.find_element(By.CSS_SELECTOR, "a.title")
            location_elem = job.find_elements(By.CSS_SELECTOR, "span.locWdth, span.loc")

            title = title_elem.text.strip()
            location = location_elem[0].text.strip() if location_elem else "Unknown"

            skills = []

            try:
                # Open job
                driver.execute_script("arguments[0].click();", title_elem)
                time.sleep(random.uniform(2, 4))

                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])

                time.sleep(random.uniform(2, 4))

                desc_elem = driver.find_elements(
                    By.CSS_SELECTOR,
                    "div.styles_JDC__dang-inner-html__h0K4t"
                )

                description = desc_elem[0].text if desc_elem else ""

                skills = extract_skills(title + " " + description)

            except Exception as e:
                print("Tab error:", e)
                skills = extract_skills(title)

            # ✅ Save job
            job_id = insert_job(title, location)

            # ✅ Save skills + linking
            for skill in skills:
                skill_id = insert_skill(skill)
                link_job_skill(job_id, skill_id)

            print(f"{index + 1}. Saved:", title)
            print("Location:", location)
            print("Skills:", skills)
            print("-" * 40)

            # Close tab safely
            try:
                if len(driver.window_handles) > 1:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print("Tab close error:", e)

            # 🔥 Restart driver every 8 jobs (fix crash issue)
            if index != 0 and index % 8 == 0:
                print("Restarting driver safely...")

                driver.quit()
                time.sleep(2)

                driver = start_driver()
                driver.get("https://www.naukri.com/data-analyst-jobs")
                time.sleep(random.uniform(4, 6))

                wait = WebDriverWait(driver, 15)

            time.sleep(random.uniform(3, 6))

            index += 1

        except Exception as e:
            print("Error in job:", e)
            index += 1

except Exception as e:
    print("Error loading jobs:", e)

driver.quit()