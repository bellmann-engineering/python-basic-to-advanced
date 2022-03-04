import csv

with open('MOCK_DATA.csv') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=',')
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        line_count += 1
        if line_count == 1:
           continue           
        else:
            #print(row[1])
            print(row['first_name'])


#addresses = dict()
#addresses = {}
#names = list()
#names = []
#paar = tuple()
#paar = ()

#https://docs.python.org/3/tutorial/datastructures.html

addresses = {'kb@bellmann-engineering.com': 'Kai', 'bill@microsoft.com': 'Bill'}
for k, v in addresses.items():
     print(k, v)

addresses['bill@microsoft.com'] = "Bill Gates"
#addresses[0] -> sorted aber nicht möglich
#addresses['bill.gates@microsoft.com'] -> key error

capitals = {"Österreich":"Wien", "Deutschland":"Berlin", "Niederlande":"Amsterdam"}
capital = capitals.pop("Schweiz","unbekannt")
if "Schweiz" in capitals: 
    print(capitals["Schweiz"])

with open('names.csv', mode='w') as csv_file:
    fieldnames = ['vorname', 'nachname']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'vorname': 'Kai', 'nachname': 'Bellmann' })
    writer.writerow({'vorname': 'Angelos', 'nachname': 'Kyrgetsos' })
