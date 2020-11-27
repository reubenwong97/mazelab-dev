from collections import namedtuple

# Can treat as if whenever u create a VonNeumannMotion "object", u can pass in
# four arguments, north, south, west and east
VonNeumannMotion = namedtuple('VonNeumannMotion', 
                              ['north', 'south', 'west', 'east'], 
                              defaults=[[-1, 0], [1, 0], [0, -1], [0, 1]])


MooreMotion = namedtuple('MooreMotion', 
                         ['north', 'south', 'west', 'east', 
                          'northwest', 'northeast', 'southwest', 'southeast'], 
                         defaults=[[-1, 0], [1, 0], [0, -1], [0, 1], 
                                   [-1, -1], [-1, 1], [1, -1], [1, 1]])
