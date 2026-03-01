# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

A command-line unit converter written in Python. Supports conversions for:
- **Length**: meters, kilometers, centimeters, miles, feet, inches
- **Weight**: grams, kilograms, ounces, pounds
- **Temperature**: Celsius, Fahrenheit, Kelvin

No external dependencies — uses only the Python standard library.

## Project Structure

```
├── CLAUDE.md           # This file — guidance for AI assistants
├── pyproject.toml      # Project metadata
├── .gitignore          # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── converter.py    # Core conversion logic (convert function, unit data)
│   └── main.py         # Interactive CLI entry point
└── tests/
    ├── __init__.py
    └── test_converter.py  # Unit tests for all conversions
```

## Common Commands

```bash
# Run the converter interactively
python -m src.main

# Run all tests
python -m unittest discover tests/

# Run a specific test class
python -m unittest tests.test_converter.TestTemperatureConversions
```

## Architecture

- `src/converter.py` — Contains all conversion logic. Length and weight use multiplication factors through a base unit (meters and grams respectively). Temperature uses explicit formulas via Celsius as an intermediate.
- `src/main.py` — Interactive CLI loop. Displays numbered menus, takes user input, calls `convert()`, and prints results.
- `tests/test_converter.py` — Tests using Python's built-in `unittest`. Covers all categories, round-trip conversions, edge cases (zero, negative temps, absolute zero).

## Development Guidelines

### Git Workflow

- Use feature branches with descriptive names
- Write clear, concise commit messages that explain the "why" behind changes
- Keep commits focused on a single logical change

### Code Quality

- Prefer simple, readable code over clever abstractions
- Add tests for new functionality
- Do not introduce known security vulnerabilities (OWASP top 10)
- No external dependencies unless absolutely necessary

### Adding New Units

1. For length/weight: add the unit and its conversion factor to the appropriate dict in `src/converter.py` (`LENGTH_UNITS` or `WEIGHT_UNITS`)
2. For temperature: add conversion formulas in `_convert_temperature()`
3. Update the `CATEGORIES` dict if adding a new category
4. Add corresponding tests in `tests/test_converter.py`
