from datetime import datetime

list = [
    ["Mary Poppins", "1735-05-29", "Mallorca,Spain", "Balenciaga"],
    ["Henry Ford", "1822-11-14", "Jinja,Uganda", "Breitling"],
    ["Mary Blanchette", "1602-08-29", "Marrakesh,Morroco", "Addidas"],
    ["Adam Driver", "1995-12-04", "Tromso,Norway", "Pierre Cardin"],
    ["Xavier Reno", "1884-08-10", "Texas,United States", "Oracle"],
    ["Jonas Gahr", "1992-02-29", "St.George,Grenada", "Google"],
    ["Brad Olsen", "1780-05-01", "Kiwengwa,Zanzibar", "Xiaomi"],
    ["Theo Walcott", "1995-03-30", "Girona,Spain", "Hewlet-Packard"],
    ["Ryan Giggs", "1597-01-19", "Jozani,Zanzibar", "Tom and Jerry"]
]

celebrities = {}

def getAge(DOB_str):
    DOB = datetime.strptime(DOB_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
    return age

def getCity(city_country_str):
    city = city_country_str.split(",")[0].strip()
    return city

def getCountry(city_country_str):
    country = city_country_str.split(",")[1].strip()
    return country

def populate_celebrities(nested_list):
    for i, profile in enumerate(nested_list):
        Name, DOB, city_country, brand = profile
        age = getAge(DOB)
        city = getCity(city_country) 
        country = getCountry(city_country)
       
        profile_key = f"profile-{i+1}"
        celebrities[profile_key] = {
            "name": Name,
            "BirthYear": DOB,
            "Age": age,
            "City": city,
            "Country": country,
            "Brand": brand
        }

populate_celebrities(list)

# Sort celebrities profiles using  name using  alphabetical order
sorted_celebrities = dict(sorted(celebrities.items(), key=lambda item: item[1]['name']))

sorted_profiles = {}
for index, (key, profile) in enumerate(sorted_celebrities.items(), start=1):
    new_key = f"profile-{index}"
    sorted_profiles[new_key] = profile


for key, profile in sorted_profiles.items():
    print(f"{key}:")
    for attribute, value in profile.items():
        print(f"  {attribute}: {value}")
    print()
