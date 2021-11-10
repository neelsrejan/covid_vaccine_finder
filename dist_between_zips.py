import time


def get_dist_between(zipcode, curr_zip, driver):
    driver.get("https://www.freemaptools.com/distance-between-usa-zip-codes.htm")
    time.sleep(1.5)

    zip_a = driver.find_element_by_name("pointa")
    zip_a.send_keys(zipcode)

    zip_b = driver.find_element_by_name("pointb")
    zip_b.send_keys(curr_zip)

    search_btn = driver.find_element_by_css_selector(".fmtbutton")
    search_btn.click()
    time.sleep(3)

    return driver.find_element_by_css_selector("#transport").get_attribute("value")


