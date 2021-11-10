import time


def find_demo(zipcode, driver):
    driver.get("https://data.census.gov/cedsci/")
    time.sleep(2)

    search_zip = driver.find_element_by_tag_name("input")
    search_zip.send_keys(zipcode)

    search_button = driver.find_element_by_css_selector(".aqua-searchbar_search-button-outer")
    search_button.click()
    time.sleep(2)

    h2_list = driver.find_elements_by_css_selector("h2")

    has_table = False
    for h2 in h2_list:
        if h2.text == "Tables":
            has_table = True

    if not has_table:
        return [zipcode] + [None] * 19

    idx_of_age = None
    tab_list = driver.find_elements_by_css_selector("section .entry-content")
    for idx in range(len(tab_list)):
        if tab_list[idx].get_attribute("aria-label")[0:11] == "AGE AND SEX":
            idx_of_age = idx
            break

    if idx_of_age is None:
        return [zipcode] + [None] * 19

    tab_to_click = tab_list[idx_of_age]
    tab_to_click.click()
    time.sleep(4)

    pop_by_age = [zipcode]
    for idx in range(0, 20):
        row_val = driver.find_elements_by_css_selector(f'div[row-index="{idx}"] div')[1].text
        if idx != 1:
            pop_by_age.append(row_val)

    return pop_by_age


