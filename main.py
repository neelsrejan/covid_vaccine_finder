from selenium import webdriver
from get_user_wants import get_user_wants
from get_all_zips import get_all_zips
from find_locs import find_locations
from find_demo import find_demo
from dist_between_zips import get_dist_between
import pandas as pd
from datetime import date

zipcode, distance = get_user_wants()

chromedriver_path: str = r"C:\development\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)

col_names_demographics = ['Zipcode', 'Total population', 'Under 5 years', '5 to 9 years', '10 to 14 years', '15 to 19 years', '20 to 24 years', '25 to 29 years', '30 to 34 years', '35 to 39 years', '40 to 44 years', '45 to 49 years', '50 to 54 years', '55 to 59 years', '60 to 64 years', '65 to 69 years', '70 to 74 years', '75 to 79 years', '80 to 84 years', '85 years and over']
col_names_locations = ["Zipcode", "Store", "Distance"]

zipcodes = get_all_zips(zipcode, distance, driver)
df_zip_demographics = pd.DataFrame(columns=col_names_demographics)
df_zip_locations = pd.DataFrame(columns=col_names_locations)

driver.execute_script("window.open()")
driver.execute_script("window.open()")
for curr_zip in zipcodes:
    driver.switch_to.window(driver.window_handles[0])
    demographics_list = find_demo(curr_zip, driver)
    driver.switch_to.window(driver.window_handles[1])
    car_dist = get_dist_between(zipcode, curr_zip, driver)
    driver.switch_to.window(driver.window_handles[2])
    locations_list = find_locations(curr_zip, car_dist, driver)

    df_zip_demographics.loc[len(df_zip_demographics)] = demographics_list
    for location in locations_list:
        df_zip_locations.loc[len(df_zip_locations)] = location

today = date.today()
df_zip_demographics.to_csv(fr"C:\Users\neels\PycharmProjects\covid_vaccine\{zipcode}_{distance}_{today}_demographics.csv")
df_zip_locations.to_csv(fr"C:\Users\neels\PycharmProjects\covid_vaccine\{zipcode}_{distance}_{today}_locations.csv")

driver.quit()
