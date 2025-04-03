from datetime import date
from datetime import datetime
import time

seconds_since_epoch = time.time() #Get time since epoch full on
formatted_since_epoch = f"{seconds_since_epoch:,.4f}" #Format the seconds since epoch with 4 digits after comma
formatted_since_epoch_scientific = f"{seconds_since_epoch:.2e}" #Format to expo for scientific abreviation

today = date.today() #Default on Year-Month-Date in numbers
formatted_date = today.strftime("%b %d %Y") #Format to %b = reduced Month name + %d = simple numbered date + %Y full year numbered


print("Seconds since January 1, 1970:", formatted_since_epoch, "or", formatted_since_epoch_scientific, "in scientific notation")
print(formatted_date)
