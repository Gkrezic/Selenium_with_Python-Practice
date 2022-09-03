from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Browser:
    def __init__(self, teardown=False):
        self.teardown = teardown
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()
            print('Closing...')
    def open_first_page(self, url):
        self.driver.get(url)
    def change_currency_menu(self, change_currency=False, new_currency=None):
        currency_element = self.driver.find_element(By.CSS_SELECTOR,
            'button[data-tooltip-text="Odaberite valutu"]'
        )
        currency_element.click()
        if change_currency:
            selected_currency_element = self.driver.find_element(By.CSS_SELECTOR,
                f'a[data-modal-header-async-url-param*="selected_currency={new_currency}"]'
            )
            selected_currency_element.click()
        else:
            exit_currency_list = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Zatvori popis valuta"]'
            )
            exit_currency_list.click()

    def choose_your_language(self, language='English'):
        language_menu = self.driver.find_element(By.CSS_SELECTOR,
        'button[data-tooltip-text="Choose your language"]')
        language_menu.click()
        self.driver.find_element(By.XPATH,
            f"//*[contains(text(), '{language}')]"
        ).click()
    def choose_place_to_go(self, place):
        search_field = self.driver.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place)
        first_result = self.driver.find_element(By.CSS_SELECTOR,
            'li[data-i="0"]'
        )
        first_result.click()
    def check_in_date(self, date):
        check_in = self.driver.find_element(By.CSS_SELECTOR,
            f'td[data-date="{date}"]'
        )
        check_in.click()
    def check_out_date(self, date):
        check_out = self.driver.find_element(By.CSS_SELECTOR,
            f'td[data-date="{date}"]'
        )
        check_out.click()
    def number_of_guests(self, adults=2, children=0):
        self.children = children
        guests_field = self.driver.find_element(By.ID,
            'xp__guests__toggle'
        )
        guests_field.click()
        adults_number_element = self.driver.find_element(By.ID, 'group_adults')
        adults_number = int(adults_number_element.get_attribute('value'))
        children_number_element = self.driver.find_element(By.ID, 'group_children')
        children_number = int(children_number_element.get_attribute('value'))
        while adults > adults_number:
            increase_adults_number = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Povećaj broj za kategoriju \'Odrasli\'"]'
            )
            increase_adults_number.click()
            adults_number = int(adults_number_element.get_attribute('value'))
            if adults == adults_number:
                break
        while adults < adults_number:
            decrease_adults_number = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Smanji broj za kategoriju \'Odrasli\'"]'
            )
            decrease_adults_number.click()
            adults_number = int(adults_number_element.get_attribute('value'))
            if adults == adults_number:
                break
        while children > children_number:
            increase_children_number = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Povećaj broj za kategoriju \'Djeca\'"]'
            )
            increase_children_number.click()
            children_number = int(children_number_element.get_attribute('value'))
            if children == children_number:
                break
        while children > children_number:
            decrease_children_number = self.driver.find_element(By.CSS_SELECTOR,
                'button[aria-label="Smanji broj za kategoriju \'Djeca\'"]'
            )
            decrease_children_number.click()
            children_number = int(children_number_element.get_attribute('value'))
            if children == children_number:
                break
    def children_age(self, age1=0, age2=0, age3=0, age4=0, age5=0, age6=0, age7=0, age8=0, age9=0, age10=0):
        x = 0
        while self.children > 0:
            x = x + 1
            if x == 1:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 1. djeteta"]'
                                                         ))
                select.select_by_value(f'{age1}')
            if x == 2:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 2. djeteta"]'
                                                         ))
                select.select_by_value(f'{age2}')
            if x == 3:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 3. djeteta"]'
                                                         ))
                select.select_by_value(f'{age3}')
            if x == 4:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 4. djeteta"]'
                                                         ))
                select.select_by_value(f'{age4}')
            if x == 5:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 5. djeteta"]'
                                                         ))
                select.select_by_value(f'{age5}')
            if x == 6:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 6. djeteta"]'
                                                         ))
                select.select_by_value(f'{age6}')
            if x == 7:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 7. djeteta"]'
                                                         ))
                select.select_by_value(f'{age7}')
            if x == 8:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 8. djeteta"]'
                                                         ))
                select.select_by_value(f'{age8}')
            if x == 9:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 9. djeteta"]'
                                                         ))
                select.select_by_value(f'{age9}')
            if x == 10:
                select = Select(self.driver.find_element(By.CSS_SELECTOR,
                                                         '[aria-label="Dob 10. djeteta"]'
                                                         ))
                select.select_by_value(f'{age10}')
            if x == self.children:
                break
    def search(self):
        search = self.driver.find_element(By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search.click()
    def star_rating_filtration(self, stars):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, '[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for element in star_child_elements:

            if str(element.get_attribute('innerHTML')).strip() == f'{stars} zvjezdice' or str(element.get_attribute('innerHTML')).strip() == f'{stars} zvjezdica':
                element.click()

    def lowest_price_sorting(self):
        try:
            sorters_dropdown= self.driver.find_element(By.CSS_SELECTOR,
                'button[data-testid="sorters-dropdown-trigger"]'
            )
            sorters_dropdown.click()
            lowest_price_sort = self.driver.find_element(By.CSS_SELECTOR,
                'button[data-id="price"]'
            )
            lowest_price_sort.click()
        except:
            sorter_tab = self.driver.find_element(By.XPATH,
                "//*[contains(text(), 'Cijena (od najniže)')]"
            )
            sorter_tab.click()

with Browser(teardown=True) as test:
    test.open_first_page("https://www.booking.com/")
    test.choose_your_language('Hrvatski')
    test.change_currency_menu(change_currency=True, new_currency='BAM')
    test.choose_place_to_go('Mostar')
    test.check_in_date('2022-10-01') #date format YYYY-MM-DD
    test.check_out_date('2022-10-03') #date format YYYY-MM-DD
    test.number_of_guests(adults=1, children=4)
    test.children_age(age1=5, age2=7, age3=4, age4=15)
    test.search()
    test.star_rating_filtration(3)
    test.lowest_price_sorting()
    print('Everything is ok')

