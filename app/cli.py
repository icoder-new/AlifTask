from typer import run, Argument
from action import ActionType


def add_action(filename: str):
    """Adds product to file"""
    product_name = input("Enter product's name: ").lower()

    price = input("Enter product's new price: ")

    try:
        price = int(price)
    except ValueError:
        print(f"Invalid price given {price}")

    with open(filename, mode="r") as file:
        content = file.read().lower()

        for line in content.split('\n'):
            if not line:
                break

            try:
                product, price = "".join(line.split('-')).split()
            except Exception as e:
                print(f"Exception occur during splitting line {e}")
                exit(-1)

            if product == product_name:
                print(f"Product {product_name} already exist!")
                exit(-3)

    with open(filename, mode='a') as f:
        f.write(f"{product_name} - {price} \n")


def change_action(filename: str):
    """
    Changes value from file
    :param filename: A filename
    :return:
    """
    product_name = input("Enter product's name: ").lower()
    new_price = input("Enter product's new price: ")
    found = False
    new_content = ""

    with open(filename, mode="r") as file:
        content = file.read().lower()

        for line in content.split('\n'):
            if not line:
                break

            try:
                product, price = "".join(line.split('-')).split()
            except Exception as e:
                print(f"Exception occur during splitting line {e}")
                exit(-1)

            if product == product_name:
                found = True
                new_content += f"{product} - {new_price}\n"
                continue

            new_content += f"{product} - {price}\n"

    if not found:
        print(f"Error, product {product_name} not found.")
        exit(-2)

    with open(filename, mode='w') as f:
        f.write(new_content)


def remove_action(filename: str):
    """Removes a product from file"""

    product_name = input("Enter product's name: ").lower()
    new_content = ""

    with open(filename, mode="r") as file:
        content = file.read().lower()

        for line in content.split('\n'):
            if not line:
                break

            try:
                product, price = "".join(line.split('-')).split()
            except Exception as e:
                print(f"Exception occur during splitting line {e}")
                exit(-1)

            if product != product_name:
                new_content += f"{product} - {price}\n"

    with open(filename, mode='w') as f:
        f.write(new_content)


def calculate_action(filename: str):
    """
    Calculates a total price
    :param filename: A filename
    """
    total = 0

    with open(filename, mode="r") as file:
        content = file.read().lower()

        for line in content.split('\n'):
            if not line:
                break

            try:
                product, price = "".join(line.split('-')).split()
            except Exception as e:
                print(f"Exception occur during splitting line {e}")
                exit(-1)

            # Also, convert to float
            try:
                price = float(price)
            except ValueError:
                print(f"Invalid value {price}")

            total += price

    print(f"Total: {total}")


def main(filename: str = Argument(..., help="Just filename with commands"), action: str = Argument(..., help="Action")):
    """Main function of program"""

    act_type = ActionType.from_string(action)

    match act_type:
        case ActionType.ADD:
            add_action(filename)
        case ActionType.CHANGE:
            change_action(filename)
        case ActionType.REMOVE:
            remove_action(filename)
        case ActionType.CALCULATE:
            calculate_action(filename)


def cli():
    """Runs main"""
    run(main)


if __name__ == '__main__':
    cli()
