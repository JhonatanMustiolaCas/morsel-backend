from unicodedata import normalize
import re


def clean_accents(source: str):
    # -> NFD y eliminar diacríticos
    cleaned_str = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+",
        r"\1",
        normalize("NFD", source),
        0,
        re.I,
    )

    # -> NFC
    cleaned_str = normalize("NFC", cleaned_str)
    return cleaned_str
