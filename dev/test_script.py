import game as g

r = g.Game(5,12)
r.print()

print(r.add_item("rock", 2,1))
print(r.add_item("rock", 3,3))
print(r.add_item("pebble", 3,3))
print(r.add_item("rock", 3,5))

print(r.add_item("fish", 2,2))

r.print()
print (r.contains(2,2))
print (r.contains(3,3))

