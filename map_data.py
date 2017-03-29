import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from PIL import Image, ImageTk

# Create a map from the basemap
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# Load the shapefile, using the name 'states'
map.readshapefile('images/shapefiles/st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can look up the shape object for a state by name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
          "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
          "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
          "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
          "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
          "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# Saves a map of all coins currently collected
# (must close and reopen program for changes to show)
def get_overall_map(list):
    for x in list:
        # Get current axes instance
        ax = plt.gca()
        # Get state and draw the filled polygon
        seg = map.states[state_names.index(x)]
        poly = Polygon(seg, facecolor='red', edgecolor='red')
        ax.add_patch(poly)

    # Save file in images/map
    savefig('images/map/master.png', bbox_inches='tight')


# Saves a map for each state with just that state filled-in
def get_state_maps(list):
    counter = 0
    for x in list:
        ax = plt.gca()
        seg = map.states[state_names.index(x)]
        poly = Polygon(seg, facecolor='red', edgecolor='red')
        ax.add_patch(poly)
        savefig('images/map/map' + str(counter) + '.png', bbox_inches='tight')
        poly.set_facecolor('None')
        poly.set_edgecolor('None')
        counter += 1
