# code by khuyen.le-minh@jobseeker.vn
# i'm learning python from basic

import csv
f = raw_input("Path to the *.csv file: ")
rows = csv.reader(open(f, "rb"))
new_rows = []
for row in rows:
    if row not in new_rows:                                              
        new_rows.append(row)
writer = csv.writer(open(f, "wb"))
writer.writerows(new_rows)
print 'Done checking!'
