# Conversion factors to a base unit for each category.
# Length base unit: meters
# Weight base unit: grams

LENGTH_UNITS = {
    "meters": 1.0,
    "kilometers": 1000.0,
    "centimeters": 0.01,
    "miles": 1609.344,
    "feet": 0.3048,
    "inches": 0.0254,
}

WEIGHT_UNITS = {
    "grams": 1.0,
    "kilograms": 1000.0,
    "ounces": 28.3495,
    "pounds": 453.592,
}

CATEGORIES = {
    "length": list(LENGTH_UNITS.keys()),
    "weight": list(WEIGHT_UNITS.keys()),
    "temperature": ["celsius", "fahrenheit", "kelvin"],
}


def convert(value, from_unit, to_unit, category):
    """Convert a numeric value from one unit to another within a category."""
    if from_unit == to_unit:
        return value

    if category == "length":
        return _convert_with_factors(value, from_unit, to_unit, LENGTH_UNITS)
    elif category == "weight":
        return _convert_with_factors(value, from_unit, to_unit, WEIGHT_UNITS)
    elif category == "temperature":
        return _convert_temperature(value, from_unit, to_unit)
    else:
        raise ValueError(f"Unknown category: {category}")


def _convert_with_factors(value, from_unit, to_unit, factors):
    """Convert using multiplication factors through a base unit."""
    base_value = value * factors[from_unit]
    return base_value / factors[to_unit]


def _convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    # First convert to Celsius
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Then convert from Celsius to target
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")
