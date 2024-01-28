import csv

def csv_parser(name):
    with open(name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        items = []

        for row in reader:
            # make a list of dictionaries
            product = {}

            for i, value in enumerate(header):
                product[value] = row[i]

            items.append(product)

        return items
