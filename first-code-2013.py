import csv

csv_folder = "/Users/Editorial/downloads/"

# this file has the original credits in html without unit id 
in_file = open(csv_folder + 'credits2.csv', "rU")
reader = csv.reader(in_file)

#this is where the units with the # will get assigned
out_file = open(csv_folder + 'creditsforupload.csv', "w")
writer = csv.writer(out_file)

#this file has unit names and id
keyfile = csv.reader(open(csv_folder + 'units-id-name.csv', 'rU'))

# turning it into a unit name/ id dictionary, and id / credit dictionary
name_id = {}
id_credit = {}

for row in keyfile:
	name, id = row
	name_id[name] = id
	print (name, id)

#looking up column 1 of credits2.csv against keys in my unit/id dictionary, getting rid of the names from the html once it matches, and then merging all credits for each unit into a single cell by using a dictionary

for row in reader:
	for name in name_id: 
		if name + " " in row[0]:
			id = name_id[name]
			if id in id_credit:
				id_credit[id] += row[0].replace("for " + name + " by", "by")
			else:
				id_credit[id] = row[0].replace("for " + name + " by", "by")



for id in id_credit:
	row[0] = id
	row[1] = id_credit[id]
	print (row[0], row[1])
	writer.writerow(row)



in_file.close()    
out_file.close()