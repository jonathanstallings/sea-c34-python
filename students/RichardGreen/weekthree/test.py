from collections import defaultdict

# data = [(2010, 2), (2009, 4), (1989, 8), (2009, 7)]

donor_info = [('Doug Peters', 150), ('Gene Simmons', 1000), ('Julie Andrews', 500), ('Guy Ritchie', 0)]


# donor_info = {"Doug Peters": 150,"Gene Simmons": 1000, "Julie Andrews": 500, "Guy Ritchie": 0, "Paul Allen": 0}

new_donors = [('Paul Allen', 5000), ('Doug Peters', 100), ('Gene Simmons', 250)]

print "Before"
print donor_info

d = defaultdict(list)


for key, value in donor_info:
    d[key].append(value)

# donor_info
# = new_donors()


# for line in new_donors:
#     if line in donor_info:
#         # append the donation to the existing array at this slot
#         donor_info[line[0]].append(line[1])
#     else:
#         # create a new array in this slot
#         donor_info[line[0]] = [line[1]]

print "After"
print d


#results_sum = {}

# for key, value in d.iteritems():
#         if key == ["Simmons", "Kent"]:
#             print key
#             #results_sum[key] = sum(value)
#         #print results_sum


# results_sum[value] = sum(key)
