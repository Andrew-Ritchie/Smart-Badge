import game as g

r = g.Game(5,12, debugger = True)
r.print()

r.add_item("rock", 2,1)
r.add_item("rock", 3,3)
r.add_item("pebble", 3,3)
r.add_item("rock", 3,5)

r.add_item("fish", 2,2)

r.print()
print(r.present_at(2,2))
print(r.present_at(3,3))

r.print()
r.move_all("right", 2)
r.print()
r.move_all("right", 5)
r.print()
r.move_all("right", 4, roll_over=True)
r.print()
