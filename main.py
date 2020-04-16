from selenium import webdriver
from app.login import Login
from app.consignment import Consignment



path = "path/your/driver"
rndc_url = "https://rndc.mintransporte.gov.co/MenuPrincipal/tabid/204/language/es-MX/Default.aspx?returnurl=%2fes-mx%2fprogramasrndc%2fcreardocumento.aspx"
driver = webdriver.Chrome(path)
driver.get(rndc_url)


username = "****"
password = "****"
travel_id = "125942"


login = Login(driver)
consignment = Consignment(driver)
login.ingress_to_rndc(username, password)
consignment.generate_consignment()
consignment.fill_preliminary_info(travel_id)