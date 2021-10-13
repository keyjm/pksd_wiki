import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.locators_wiki import WikiPageLocators


class WikiPage(WikiPageLocators):

    # Chromedriver instance. Normally would create this in a seperate class a webdriver factory and also include
    # options for other browsers
    driver = webdriver.Chrome()

    def open_wikipage(self):
        self.driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")

    def get_contents_headings(self):
        headings_list = []
        content_headings = self.driver.find_elements_by_xpath(self.CONTENT_HEADINGS_LOC)
        for i in content_headings:
            headings_list.append(i.text)
        return headings_list

    def get_page_headings(self):
        headings_list = []
        mod_heading_list = []
        page_headings = self.driver.find_elements_by_xpath(self.PAGE_HEADINGS_LOC)
        for i in page_headings:
            headings_list.append(i.text)
        for i in headings_list:
            xyz = i[:-6]
            mod_heading_list.append(xyz)
        return mod_heading_list

    def get_content_links(self):
        content_links = self.driver.find_elements_by_xpath(self.CONTENT_LINKS_LOC)
        for link in content_links:
            r = requests.head(link.get_attribute('href'))
            if r.status_code != 200:
                raise Exception(f"{link}-->{r.status_code}")
            else:
                return True

    def personified_concept_nike_text(self):
        elem = self.driver.find_element_by_xpath(self.PERSONIFIED_CONCEPT_NIKE_LOC)
        hov = ActionChains(self.driver).move_to_element(elem)
        hov.perform()
        txt = self.driver.find_element_by_xpath(self.NIKE_POP_UP_LOC)
        print(txt)

    def nike_family_tree_present(self):
        elem = self.driver.find_element_by_xpath(self.NIKE_LINK_LOC)
        elem.click()
        wait = WebDriverWait(self.driver, 10)
        is_family_tree_visible = wait.until(ec.visibility_of_element_located((By.XPATH, self.NIKE_FAMILY_TREE_IMG)))
        if is_family_tree_visible is None:
            return False
        else:
            return True

    def close_browser(self):
        self.driver.quit()
