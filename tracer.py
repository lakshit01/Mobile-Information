import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your number with country code : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carier = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print(carier)
print(reg)
