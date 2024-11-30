import csv
def save_employee(filename, data, headers):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"Data saved to {filename}")
def read_employees(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader, [])
        data = [row for row in reader if row]
        return headers, data
def update_csv(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Data updated in {filename}")