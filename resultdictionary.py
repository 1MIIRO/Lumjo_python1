NextDictionary = {
    "Cars": ["BMW", "JEEP", "TOYOTA", "FIAT", "CHRYSLER", "FORD", 45000, 1992, 1890, 250, "18L", 6325],
    "Trucks": [1200, "CAT", "Stone-Crusher", "Sand-Mixer", 67009, 15.85, 704, 1650],
    "Planes": ["32 Seater", "Row 5A", 890, 10, 12, 2025, 700845, 70.11, "Airbus", "Boeing", 0.864002]
}


resultDictionary = {
    "Strings": [],
    "Floats": [],
    "Integers": []
}


for category, items in NextDictionary.items():
    for item in items:
        if isinstance(item, str):
            resultDictionary["Strings"].append(item)
        elif isinstance(item, int):
            resultDictionary["Integers"].append(item)
        elif isinstance(item, float):
            resultDictionary["Floats"].append(item)


print(resultDictionary)
