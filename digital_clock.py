#!/usr/bin/env python
# Defines the visual representation of large, user-provided digits for the timer.

# Each character is represented as a 9-line string.
LARGE_DIGITS = {
    '0': (
        " ###### ",
        "###  ###",
        "##    ##",
        "##    ##",
        "##    ##",
        "##    ##",
        "##    ##",
        "###  ###",
        " ###### "
    ),
    '1': (
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   ",
        "   ##   "
    ),
    '2': (
        " ###### ",
        "##    ##",
        "      ##",
        "      ##",
        "########",
        "##      ",
        "##      ",
        "##    ##",
        "########"
    ),
    '3': (
        " ###### ",
        "##    ##",
        "      ##",
        "      ##",
        " #######",
        "      ##",
        "      ##",
        "##    ##",
        " ###### "
    ),
    '4': (
        "##    ##",
        "##    ##",
        "##    ##",
        "##    ##",
        " #######",
        "      ##",
        "      ##",
        "      ##",
        "      ##"
    ),
    '5': (
        "########",
        "##     #",
        "##      ",
        "##      ",
        "########",
        "      ##",
        "      ##",
        "##    ##",
        " ###### "
    ),
    '6': (
        " ###### ",
        "##    ##",
        "##      ",
        "##      ",
        "####### ",
        "##    ##",
        "##    ##",
        "##    ##",
        " ###### "
    ),
    '7': (
        "########",
        "#     ##",
        "      ##",
        "      ##",
        "  ######",
        "      ##",
        "      ##",
        "      ##",
        "      ##"
    ),
    '8': (
        " ###### ",
        "##    ##",
        "#      #",
        "##    ##",
        " ###### ",
        "##    ##",
        "#      #",
        "##    ##",
        " ###### "
    ),
    '9': (
        " ###### ",
        "##    ##",
        "#      #",
        "##    ##",
        " #######",
        "      ##",
        "      ##",
        "##    ##",
        " ###### "
    ),
    ':': (
        "    ",
        " ## ",
        " ## ",
        " ## ",
        "    ",
        " ## ",
        " ## ",
        " ## ",
        "    "
    ),
    ' ': (
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        "
    )
}

def generate_clock_text(time_str: str) -> str:
    """Assembles a multi-line string representing the time with large digits."""
    lines = ['' for _ in range(9)]
    for char in time_str:
        # Default to a space if a character is not in the dictionary
        digit_lines = LARGE_DIGITS.get(char, LARGE_DIGITS[' '])
        for i in range(9):
            lines[i] += digit_lines[i] + " "
    return "\n".join(lines)