# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Project Overview

A unit converter and tax calculator available as both a **web app** and a **command-line tool**. Supports conversions for:
- **Length**: meters, kilometers, centimeters, miles, feet, inches
- **Weight**: grams, kilograms, ounces, pounds
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Tax Calculator**: compute tax from a subtotal, or reverse-calculate a pre-tax price from a total (includes US state preset rates)

No external dependencies required.

## Project Structure

```
├── CLAUDE.md           # This file — guidance for AI assistants
├── index.html          # Web app (single file, works in any browser)
├── pyproject.toml      # Project metadata
├── .gitignore          # Git ignore rules
├── src/
│   ├── __init__.py
│   ├── converter.py    # Core conversion logic (Python, convert function, unit data)
│   ├── tax.py          # Tax calculation logic (calculate_tax, calculate_pretax, preset rates)
│   └── main.py         # Interactive CLI entry point (Python)
└── tests/
    ├── __init__.py
    ├── test_converter.py  # Unit tests for all conversions
    └── test_tax.py        # Unit tests for tax calculations
```

## Common Commands

```bash
# Open the web app — just open index.html in a browser

# Run the CLI converter interactively
python -m src.main

# Run all tests
python -m unittest discover tests/

# Run a specific test class
python -m unittest tests.test_converter.TestTemperatureConversions
```

## Architecture

- `index.html` — Self-contained web app with embedded CSS and JavaScript. Mobile-friendly responsive design. Conversion logic is duplicated in JS to keep the web app dependency-free.
- `src/converter.py` — Python conversion logic. Length and weight use multiplication factors through a base unit (meters and grams respectively). Temperature uses explicit formulas via Celsius as an intermediate.
- `src/tax.py` — Tax calculation logic. `calculate_tax()` computes tax from a subtotal; `calculate_pretax()` reverse-calculates the pre-tax price from a total. Includes `PRESET_TAX_RATES` dict with common US state rates.
- `src/main.py` — Interactive CLI loop. Displays numbered menus, takes user input, calls `convert()`, and prints results. Also includes a tax calculator sub-menu.
- `tests/test_converter.py` — Tests using Python's built-in `unittest`. Covers all categories, round-trip conversions, edge cases (zero, negative temps, absolute zero).
- `tests/test_tax.py` — Tests for tax calculations: forward/reverse calculations, rounding, edge cases, and preset rate validation.

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
4. Mirror the changes in the `units` object and `convertTemperature()` function in `index.html`
5. Add corresponding tests in `tests/test_converter.py`
