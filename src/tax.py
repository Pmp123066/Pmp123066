# Tax calculation utilities.
# Supports calculating tax from a subtotal, and reverse-calculating
# the pre-tax price from a total that already includes tax.

# Common US state sales tax rates (2026) for quick reference.
# Users can always enter a custom rate.
PRESET_TAX_RATES = {
    "California": 7.25,
    "Texas": 6.25,
    "New York": 4.0,
    "Florida": 6.0,
    "Illinois": 6.25,
    "Pennsylvania": 6.0,
    "Ohio": 5.75,
    "Georgia": 4.0,
    "Washington": 6.5,
    "No tax (OR, MT, NH, DE)": 0.0,
}


def calculate_tax(subtotal, tax_rate):
    """Calculate the tax amount and total from a pre-tax subtotal.

    Args:
        subtotal: The pre-tax price (must be >= 0).
        tax_rate: The tax rate as a percentage (e.g. 7.25 for 7.25%).

    Returns:
        A dict with 'subtotal', 'tax_rate', 'tax_amount', and 'total'.

    Raises:
        ValueError: If subtotal is negative or tax_rate is negative.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")

    tax_amount = round(subtotal * tax_rate / 100, 2)
    total = round(subtotal + tax_amount, 2)

    return {
        "subtotal": round(subtotal, 2),
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total": total,
    }


def calculate_pretax(total, tax_rate):
    """Reverse-calculate the pre-tax subtotal from a total that includes tax.

    Args:
        total: The total price including tax (must be >= 0).
        tax_rate: The tax rate as a percentage (e.g. 7.25 for 7.25%).

    Returns:
        A dict with 'subtotal', 'tax_rate', 'tax_amount', and 'total'.

    Raises:
        ValueError: If total is negative or tax_rate is negative.
    """
    if total < 0:
        raise ValueError("Total cannot be negative")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")

    subtotal = round(total / (1 + tax_rate / 100), 2)
    tax_amount = round(total - subtotal, 2)

    return {
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total": round(total, 2),
    }
