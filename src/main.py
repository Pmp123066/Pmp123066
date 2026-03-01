from src.converter import CATEGORIES, convert
from src.tax import PRESET_TAX_RATES, calculate_tax, calculate_pretax


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


def get_amount(prompt):
    """Prompt the user for a dollar amount."""
    while True:
        try:
            value = float(input(f"\n{prompt}: $"))
            if value < 0:
                print("Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_tax_rate():
    """Let the user pick a preset tax rate or enter a custom one."""
    presets = list(PRESET_TAX_RATES.keys())
    options = presets + ["custom rate"]
    choice = display_menu("Choose a tax rate:", options)

    if choice == "custom rate":
        while True:
            try:
                rate = float(input("\nEnter tax rate (%): "))
                if rate < 0:
                    print("Tax rate cannot be negative.")
                    continue
                return rate
            except ValueError:
                print("Please enter a valid number.")
    else:
        rate = PRESET_TAX_RATES[choice]
        print(f"\n  Using {choice}: {rate}%")
        return rate


def run_tax_calculator():
    """Run the tax calculator sub-menu."""
    print("\n" + "=" * 40)
    print("       TAX CALCULATOR")
    print("=" * 40)

    modes = ["calculate tax from subtotal", "find pre-tax price from total", "back"]
    mode = display_menu("What would you like to do?", modes)

    if mode == "back":
        return

    rate = get_tax_rate()

    if mode == "calculate tax from subtotal":
        subtotal = get_amount("Enter pre-tax amount")
        result = calculate_tax(subtotal, rate)
        print(f"\n  Subtotal:  ${result['subtotal']:.2f}")
        print(f"  Tax ({result['tax_rate']}%): ${result['tax_amount']:.2f}")
        print(f"  ─────────────────────")
        print(f"  Total:     ${result['total']:.2f}")
    else:
        total = get_amount("Enter total (with tax included)")
        result = calculate_pretax(total, rate)
        print(f"\n  Total:     ${result['total']:.2f}")
        print(f"  Tax ({result['tax_rate']}%): ${result['tax_amount']:.2f}")
        print(f"  ─────────────────────")
        print(f"  Subtotal:  ${result['subtotal']:.2f}")


def main():
    """Run the interactive unit converter."""
    print("=" * 40)
    print("     UNIT CONVERTER & TOOLS")
    print("=" * 40)

    while True:
        categories = list(CATEGORIES.keys())
        all_options = categories + ["tax calculator", "quit"]
        choice = display_menu("Choose a category:", all_options)

        if choice == "quit":
            print("\nGoodbye!")
            break

        if choice == "tax calculator":
            run_tax_calculator()
            continue

        category = choice
        units = CATEGORIES[category]

        from_unit = display_menu("Convert from:", units)
        to_unit = display_menu("Convert to:", units)
        value = get_value()

        result = convert(value, from_unit, to_unit, category)
        print(f"\n  >>> {value:g} {from_unit} = {result:g} {to_unit}")


if __name__ == "__main__":
    main()
