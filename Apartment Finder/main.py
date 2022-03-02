from apartments_data import ApartmentsData
from selenium_form import form_fill

AD = ApartmentsData()
FF = form_fill()
all_data = AD.get_data()

for data in all_data:
    FF.fill_form(data[0], data[1], data[2])
