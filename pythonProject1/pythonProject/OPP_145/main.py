from prettytable import PrettyTable
table = PrettyTable()

# Row by row
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# x.add_row(["Brisbane", 5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])


# All rows at once
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )

#Column by column
table.add_column("Pokémon Name",["Pikachu","Squirtle","Chamander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = "l"



print(table)













# import turtle
# from turtle import Turtle,Screen
# import new_module
# print(new_module.another_variable)
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# timmy.forward(100)
# #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

