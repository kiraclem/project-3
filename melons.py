# IMPORTS:
import csv

# CLASSES:
class Melon():
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = False

    def __repr__(self):
        return( 
            f"<Melon: {self.melon_id}, {self.common_name}>" )

    def price_str(self):
        return(f"${self.price:.2f}")


# DICTIONARIES:
melon_dict = {}

with open('melons.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row['melon_id']
        melon = Melon(
            melon_id,
            row['common_name'],
            float(row['price']),
            row['image_url'],
            row['color'],
            eval(row['seedless']))

        melon_dict[melon_id] = melon

print(melon_dict)

# FUNCTIONS:
def find_melon_by_id(melon_id): 
    return melon_dict[melon_id]

def get_all_melons():
    return list(melon_dict.values())

get_all_melons()