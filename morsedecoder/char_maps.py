from .constants import PATTERNS_AND_CHAR_MAPS
from .exceptions import InvalidCharMap


def get_char_map(char_map_option: str):

    options = PATTERNS_AND_CHAR_MAPS.keys()

    if char_map_option in options:
        return PATTERNS_AND_CHAR_MAPS.get(char_map_option)

    else:
        raise InvalidCharMap(f"Invalid option for {char_map_option}")
