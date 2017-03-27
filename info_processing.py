import re
import json
import os
import urllib.request

all_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
              "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
              "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]


# Returns state names in the order in the document
def get_states():
    states_reordered = []
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        for line in f:
            if line.title().strip() in all_states:
                states_reordered.append(line.title().strip())

    return states_reordered


# Returns the dates each coin was released into circulation
def get_dates():
    dates = []
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        for line in f:
            if 'Coin Release' in line:
                date = re.findall("Release: (.*) Release", line, re.DOTALL)
                dates.append(date[0])

    return dates


# Returns each coin's design description
# TODO many design descriptions are on multiple lines and don't have a universal stop character. Must deal with this
def get_descriptions():
    years = ["1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"]
    descriptions = []
    final = []
    description = ""
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        try:
            for line in f:
                if 'Design: ' in line:
                    description = (re.findall("Design: (.*) ", line, re.DOTALL)) + (re.findall("\s(\w+)$", line, re.DOTALL))
                    nextline = next(f).strip()
                    while (nextline.title() not in all_states) and (nextline not in years):
                        description.append(nextline)
                        nextline = next(f).strip()
                    descriptions.append(description)
        except:
            descriptions.append(description)

    for x in descriptions:
        concat = ' '.join(x)
        final.append(concat)

    return final


# Returns a list of links to each coin's image
def get_links_list():
    link_start = "https://www.usmint.gov/images/mint_programs/50sq_program/states/"
    link_end = "_Designs.gif"
    states = ["DE", "PA", "NJ", "GA", "CT", "MA", "MD", "SC", "NH", "VA", "NY", "NC", "RI", "VT", "KY", "TN", "OH",
              "LA", "IN", "MS", "IL", "AL", "ME", "MO", "AR", "MI", "FL", "TX", "IA", "WI", "CA", "MN", "OR", "KS",
              "WV", "NV", "NE", "CO", "ND", "SD", "MT", "WA", "ID", "WY", "UT", "OK", "NM", "AZ", "AK", "HI"]
    links = []

    for x in states:
        new_link = link_start + x + link_end
        links.append(new_link)

    return links


# Downloads each image, the links to which are generated from the method get_links_list above
def download_images():
    links = get_links_list()
    for x in range(len(links)):
        urllib.request.urlretrieve(links[x], "images/coin" + str(x) + ".gif")


# Dumps info gathered from the above methods into a JSON file
def json_dump():
    ids = []
    for x in range(50):
        ids.append(x + 1)

    states = get_states()
    dates_issued = get_dates()
    descriptions = get_descriptions()
    links = get_links_list()

    data = []
    for x in range(50):
        to_add = {"id": ids[x], "state": states[x], "date_issued": dates_issued[x],
                  "description": "todo", "image": links[x], "collected": 0}
        data.append(to_add)

    with open('data.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=2)


# Reads the JSON file created in the above method
def json_load():
    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data
