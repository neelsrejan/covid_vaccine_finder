import time


def get_all_zips(zipcode, distance, driver):
    driver.get("https://www.freemaptools.com/find-zip-codes-inside-radius.htm")
    time.sleep(1.5)

    miles = driver.find_element_by_css_selector("#tb_radius_miles")
    miles.clear()
    miles.send_keys(distance)

    zip_to_search = driver.find_element_by_css_selector("#locationSearchTextBox")
    zip_to_search.send_keys(zipcode)

    find_zips_near = driver.find_element_by_css_selector("#locationSearchButton")
    find_zips_near.click()
    time.sleep(1.5)

    return driver.find_element_by_css_selector("#tb_output").get_attribute("value").split(",")

