# beths_tunes = [
#     "The Lathums - The Great Escape",
#     "Bowling for Soup - 1985",
#     "Adele - My Little Love"
# ]

# print(beths_tunes)


website_list = [
    "Facebook",
    "Twitter",
    "Wikipedia"
]

print(website_list)

website_list.append("YouTube")
website_list.append("eBay")

print(website_list)

website_list.pop()

print(website_list)


favourite_artists = [
    "Adele",
    "Ed Sheeran",
    "The Lathums",
    "The Beatles",
    "Blink-182"
]

print(favourite_artists)

favourite_artists.sort()
print(favourite_artists)

favourite_artists.reverse()
print(favourite_artists)

favourite_artists.remove("The Beatles")
print(favourite_artists)

more_artists = [
    "Thxlo",
    "P!nk",
    "My Chemical Romance",
    "Blink-182"
]

favourite_artists.extend(more_artists)
print(favourite_artists)

counting_artists = favourite_artists.count("Blink-182")
print(counting_artists)


