from selenium.webdriver.common.by import By
from scraper.scraper_utils import start_driver
from scraper.skill_extractor import extract_skills
from database.db_connection import insert_job
import time
import random


queries = [
    "data analyst",
    "business analyst",
    "data analyst python"
]


for query in queries:

    driver = start_driver()

    search_query = query.replace(" ", "+")

    # ✅ Use India domain (less blocking)
    url = f"https://in.indeed.com/jobs?q={search_query}&l=India"

    print("\n==============================")
    print("Scraping:", query)
    print("==============================")

    driver.get(url)

    # ✅ Random delay
    time.sleep(random.randint(6, 10))

    # ✅ Scroll (important)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    jobs = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")

    print("Jobs found:", len(jobs))


    for job in jobs:
        try:
            # ✅ Safe click
            driver.execute_script("arguments[0].click();", job)
            time.sleep(random.randint(2, 4))

            # Title
            title_elem = job.find_elements(By.CSS_SELECTOR, "h2 span")
            if not title_elem:
                continue

            title = title_elem[0].text.strip()
            if title == "":
                continue

            # Location
            location_elem = job.find_elements(
                By.CSS_SELECTOR,
                "div.companyLocation, span[data-testid='text-location']"
            )
            location = location_elem[0].text.strip() if location_elem else "Unknown"

            # ✅ Description (RIGHT PANEL)
            desc_elem = driver.find_elements(By.CSS_SELECTOR, "#jobDescriptionText")
            description = desc_elem[0].text if desc_elem else ""

            # ✅ Extract skills from DESCRIPTION
            skills = extract_skills(description)

            # Save to DB
            insert_job(title, location)

            print("Saved:", title)
            print("Location:", location)
            print("Skills:", skills)
            print("-" * 40)

        except Exception as e:
            print("Error:", e)

    driver.quit()

    # ✅ Delay between queries
    time.sleep(random.randint(8, 15))