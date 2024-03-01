name = "Rayanul Kader"

first_name = name[0:7:1]
last_name = name[8:]

print(first_name)
print(last_name)

iterating_name = name[0::2]
print(iterating_name)

reverse = name[::-1]
print(reverse)

name2 = "rayanul kader chowdhury abid"
print(name2[::-1])
#Slicing object(creates blueprint that can be impliment over and over)

website_1 = "https://www.google.com"
website_2 = "https://www.wikipedia.com"

slice= slice(12,-4,1)

print(website_1[slice])
print(website_2[slice])
