import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import Select


class Consignment:
    
    def __init__(self, driver):
        self.driver = driver
        self.action_chain = action_chains.ActionChains(self.driver)

    def generate_consignment(self):
        generate_tab = self.driver.find_element_by_id("tddnn_dnnSOLPARTMENU_ctldnnSOLPARTMENU87")
        self.action_chain.move_to_element(generate_tab).perform()
        consignment_tab = self.driver.find_element_by_id("tddnn_dnnSOLPARTMENU_ctldnnSOLPARTMENU88")
        consignment_tab.click()
    
    def fill_preliminary_info(self, travel_id):
        travel_selector = Select(
            self.driver.find_element_by_id("dnn_ctr396_Remesa_REMORDENCARGALISTA")
        )
        travel_selector.select_by_value(travel_id)
        time.sleep(5.0)
        load_info_selector = Select(
            self.driver.find_element_by_id("dnn_ctr396_Remesa_CONSECUTIVOINFORMACIONCARGAL")
        )
        load_info_options = load_info_selector.options
        first_option = load_info_options[1]
        load_info_selector.select_by_value(first_option.get_attribute("value"))
        
        