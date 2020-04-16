""" Login to rndc system """
class Login:
    
    def __init__(self, driver):
        self.driver = driver
        

    def ingress_to_rndc(self, username, password):
        username_field = self.driver.find_element_by_id("dnn_ctr580_FormLogIn_edUsername")
        password_field = self.driver.find_element_by_id("dnn_ctr580_FormLogIn_edPassword")
        ingress_btn = self.driver.find_element_by_id("dnn_ctr580_FormLogIn_btIngresar")
        username_field.send_keys(username)
        password_field.send_keys(password)
        ingress_btn.click()
