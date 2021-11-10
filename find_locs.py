import time


def find_locations(zipcode, car_dist, driver):
    driver.get("https://vaccinefinder.org/search/")
    time.sleep(1.5)

    zipcode_text_box = driver.find_element_by_id("zipCode")
    zipcode_text_box.send_keys(zipcode)

    menu = driver.find_element_by_css_selector(".select__control")
    menu.click()
    time.sleep(1)

    distances = [1, 5, 10, 25, 50]
    how_far_menu= driver.find_element_by_css_selector(f"#react-select-2-option-{distances.index(50)}")
    how_far_menu.click()
    time.sleep(0.5)

    search = driver.find_element_by_css_selector(".search-form__button-container .Button")
    search.click()
    time.sleep(2)

    try:
        place_names = driver.find_elements_by_css_selector(".sc-bXevSJ")
        place_list = [place.text for place in place_names]

        addresses = driver.find_elements_by_css_selector("span")
        zip_list = [addresses[idx].text.split()[-1] for idx in range(7, len(addresses), 2)]

        in_stock = driver.find_elements_by_css_selector(".sc-ikXwZx")
        in_stock_list = [1 if stock.text == "In Stock" else 0 for stock in in_stock]

        return [[zip_list[idx], place_list[idx], car_dist] for idx in range(50) if zipcode == zip_list[idx] and in_stock_list[idx] == 1]

    except IndexError:
        return []

