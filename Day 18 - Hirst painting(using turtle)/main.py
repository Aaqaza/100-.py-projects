"""To extract colors from an image into a color_list list, use one of the below 2 codes"""
import turtle

# import colorgram as cg
#
# color_list = cg.extract("H.jpg", 120)
# color_palette = []
#
# for count in range(len(color_list)):
#     rgb = color_list[count]
#     red = rgb.rgb.r
#     green = rgb.rgb.g
#     blue = rgb.rgb.b
#     color = (red, green, blue)
#     color_palette.append(color)
#
# print(color_palette)
# print(len(color_palette))

"""OR"""

# import colorgram as cg
#
# color_list = cg.extract("H.jpg", 120)
# color_palette = []
#
# for color in color_list:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     color_palette.append(new_color)
#
# print(color_palette)
# print(len(color_palette))


from turtle import Turtle, Screen
import random

turtle.colormode(255)
"For using color_list as the colours"

color_list = [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166),
              (209, 179, 208), (246, 218, 21), (40, 133, 242), (246, 218, 5), (207, 148, 178),
              (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75), (209, 87, 66),
              (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]

screen = Screen()
turty = Turtle()
dot_count = 100

turty.ht()
turty.penup()
turty.goto(-300.00, -265.00)
turty.speed('fastest')


for dot in range(1, dot_count + 1):
    turty.dot(20, random.choice(color_list))
    turty.fd(50)

    if dot % 10 == 0:
        turty.left(90)
        turty.fd(50)
        turty.left(90)
        turty.fd(500)
        turty.setheading(0)


screen.exitonclick()
