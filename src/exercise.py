from person import Person
import csv

def main():
    file = input("filename:")

    records = read_records_from_file(file)
    print("persons: " + str(len(records)))
    print("persons:")
    for person in records:
        print(person.get_name())

def read_records_from_file(file):
    records = []
    # write here the code for reading from file
    # and printing the read records
    try:
        f = open(file, "r")
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            records.append(Person(row[0], int(row[1])))
    except:
        print("Error")
    return records

if __name__ == '__main__':
    main()
