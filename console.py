#!/usr/bin/python3
"""Entry point of the command line Interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry point of the interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """Closes the interpreter\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Do nothing when ENTER key is pressed"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class eg 'create BaseModel'\n"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                obj = eval(f"{arg}()")
                print(obj.id)
                obj.save()
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints an object eg. show BaseModel 123232\n"""
        args = arg.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objects = BaseModel.all()
            id_exists = False

            for key, value in objects.items():
                if args[0] in key:
                    obj_id = key[len(args[0]) + 1:]
                    if args[1] == obj_id:
                        print(value)
                        id_exists = True
                        break

            if not id_exists:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance eg destroy BaseModel 342352\n"""
        args = arg.split()
        if (len(args) == 0):
            print("** class name missing **")
        elif (len(args) == 1):
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objects = BaseModel.all()
            id_exists = False

            for key, value in objects.items():
                if args[0] in key:
                    obj_id = key[len(args[0]) + 1:]
                    if args[1] == obj_id:
                        print(value)
                        del objects[key]
                        id_exists = True
                        break

            if not id_exists:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints objects based or not on the class eg-all BaseModel / all\n"""
        if arg == "":
            objects = BaseModel.all()
            obj_list = []

            for key, value in objects.items():
                obj_list.append(value.__str__())

            print(obj_list)
        elif arg in HBNBCommand.classes:
            objects = BaseModel.all()
            obj_list = []

            for key, value in objects.items():
                if arg in key:
                    obj_list.append(value.__str__())

            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update or add attribute to object\n"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objects = BaseModel.all()

            id_exists = False
            # loop through objects checking if id exists
            for key, value in objects.items():
                if args[0] in key:
                    obj_id = key[len(args[0]) + 1:]
                    if args[1] == obj_id:
                        obj = objects[key]
                        id_exists = True
                        break

            if id_exists:
                # check if attribute name was provided
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    # Remove quotes ("") from args[3] and update attribute
                    setattr(obj, args[2], args[3][1:-1])
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
