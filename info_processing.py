import re
import json


# Returns state names in the order in the document
def get_states():
    all_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
              "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
              "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
              "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
              "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
              "Wisconsin", "Wyoming"]
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
# TODO many design descriptions are on multiple lines and don't have a universal stop character. How to deal with this?
def get_descriptions():
    descriptions = []
    with open('quarter_info.txt', 'r', encoding='utf8') as f:
        for line in f:
            if 'Design: ' in line:
                description = re.findall("Design: (.*) .", line, re.DOTALL)
                descriptions.append(description[0])

    return descriptions

link_start = "https://www.usmint.gov/images/mint_programs/50sq_program/states/"
link_end = "_Designs.gif"
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
          "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
          "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


# Returns a list of links to each coin's image
# TODO put in same order as all other info
def get_links_list():
    links = []

    for x in states:
        new_link = link_start + x + link_end
        links.append(new_link)

    return links


def get_links_dict():
    links = {}

    for x in states:
        new_link = link_start + x + link_end
        links[x] = new_link

    return links


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
                  "description": "todo", "image": links[x], "collected": "false"}
        data.append(to_add)

    with open('data.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=2)


# Reads the JSON file created in the above method
def json_load():
    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data
