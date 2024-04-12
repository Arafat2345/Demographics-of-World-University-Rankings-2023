from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.timeshighereducation.com/world-university-rankings/2023/world-ranking")

columns = ["Rank", "University", "Country", "Number of Students", "Number of students per staff", "International Students", "Female:Male"]

select = driver.find_element(By.NAME, 'datatable-1_length')
select.send_keys("All")


table_rows = driver.find_elements(By.XPATH, "//table[@id='datatable-1']//tbody//tr")


data = []

for row in table_rows:
    row_info = row.find_elements(By.TAG_NAME, 'td')
    
    
    rank = row_info[0].text
    university_country = row_info[1].text.split('\n')
    university = university_country[0]
    country = university_country[1] if len(university_country) > 1 else None
    students = row_info[2].text
    staff = row_info[3].text
    InternationalStudents = row_info[4].text
    f4 = row_info[5].text
    
    if ":00" in f4:
        f4 = f4.replace(":00", "")
    
    data.append({
        "Rank": rank,
        "University": university,
        "Country": country,
        "Number of Students": students,
        "Students per staff": staff,
        "International Students": InternationalStudents,
        "Female:Male": f4
    })


unis = pd.DataFrame(data)
unis.to_csv("university_rankings.csv", index=False, encoding='utf-8-sig')
driver.quit()