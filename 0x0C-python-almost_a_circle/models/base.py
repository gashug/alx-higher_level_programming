#!/usr/bin/python3
"""defines the class Base"""
import json
import csv
import turtle

class Base():
    """"empty class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class with id

        Args:
            id (int)
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json rep of data"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json rep of data"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionary_list = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(dictionary_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
                list_instances = [cls.create(**d) for d in list_dicts]
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline='') as file:
                reader = csv.reader(file)
                objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        d = {'id': int(row[0]), 'width': int(row[1]), 'height': int(row[2]), 'x': int(row[3]), 'y': int(row[4])}
                    elif cls.__name__ == "Square":
                        d = {'id': int(row[0]), 'size': int(row[1]), 'x': int(row[2]), 'y': int(row[3])}
                    objs.append(cls.create(**d))
                return objs
        except FileNotFoundError:
            return []

        @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.bgcolor("white")
        turtle.title("Draw Shapes")
        turtle.penup()
        turtle.goto(-300, 0)

        for shape in list_rectangles + list_squares:
            turtle.setheading(0)
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            turtle.color("red")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(shape.width)
                turtle.left(90)
                turtle.forward(shape.height)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()

        turtle.hideturtle()
        turtle.done()
