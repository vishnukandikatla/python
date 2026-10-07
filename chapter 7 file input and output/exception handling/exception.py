try:
    # Trigger different errors for demonstration
    result = 10 / 2                # ZeroDivisionError
    value = int("123")              # ValueError
    my_list = [1, 2, 3]
    print(my_list[5])               # IndexError
    my_dict = {"a": 1}
    print(my_dict["b"])             # KeyError
    with open("missing.txt") as f:  # FileNotFoundError
        data = f.read()

except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")

except ValueError:
    print("❌ Invalid value provided!")

except IndexError:
    print("❌ List index out of range!")

except KeyError:
    print("❌ Dictionary key not found!")

except FileNotFoundError:
    print("❌ File does not exist!")

except Exception as e:  #it used is used for the if i dont know the error the of the program it tell the what type of error its is
    # Catch-all for any other unexpected errors
    print(f"❌ An unexpected error occurred: {e}")
