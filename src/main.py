from src.converter import CATEGORIES, convert


def display_menu(title, options):
    """Display a numbered menu and return the user's choice."""
    print(f"\n{title}")
    print("-" * len(title))
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option.capitalize()}")
    print()

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a valid number.")


def get_value():
    """Prompt the user for a numeric value."""
    while True:
        try:
            return float(input("\nEnter the value to convert: "))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Run the interactive unit converter."""
    print("=" * 40)
    print("       UNIT CONVERTER")
    print("=" * 40)

    while True:
        categories = list(CATEGORIES.keys())
        quit_options = categories + ["quit"]
        choice = display_menu("Choose a category:", quit_options)

        if choice == "quit":
            print("\nGoodbye!")
            break

        category = choice
        units = CATEGORIES[category]

        from_unit = display_menu("Convert from:", units)
        to_unit = display_menu("Convert to:", units)
        value = get_value()

        result = convert(value, from_unit, to_unit, category)
        print(f"\n  >>> {value:g} {from_unit} = {result:g} {to_unit}")


if __name__ == "__main__":
    main()
