symbols = '$¢£¥€¤'

#ord changes characters from symbols their unicode number
codes = [ord(symbol) for symbol in symbols]
print("codes for the following symbols, $¢£¥€¤", codes)

beyond_ascii_codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print("codes for the following symbols, $¢£¥€¤", beyond_ascii_codes)

print("original not characters beyond 127", set(codes) ^ set(beyond_ascii_codes))
print("original and symmetric difference ofcharacters beyond 127", 
      set(codes).symmetric_difference(beyond_ascii_codes))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print("a listcomp built from colors then on sizes", tshirts)

tuple(ord(symbol) for symbol in symbols)

import array
array.array('I', (ord(symbol) for symbol in symbols))

#example of a generator function
for tshirt in ('%s %s How cool' % (c, s) for c in colors for s in sizes):
    print(tshirt)

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
  ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport) 

for country, _ in traveler_ids:
    print(country)

// declare variables
a, b = 7, 8

switch them without a temp
b, a = 8, 7


