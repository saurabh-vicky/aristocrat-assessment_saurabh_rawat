import csv


def save_data(name, price):
    with open("../products.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "price"])  # header

        for name, price in zip(name, price):
            writer.writerow([name, price])
