import csv

def view_attendance():
    records = []
    try:
        with open('attendance.csv', 'r') as att_file:
            reader = csv.reader(att_file)
            for row in reader:
                records.append(', '.join(row))
    except FileNotFoundError:
        records.append("No attendance records found.")
    return records