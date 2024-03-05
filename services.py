from morsedecoder.decoder import Decoder


def from_plain_text_to_morse_standard(source: str, include_symbols):
    char_map = "std"
    char_map += "sym" if include_symbols else ""
    decoder = Decoder(source=source, char_map=char_map, direction="tm")
    return decoder.get_result()


def from_plain_text_to_morse_es(source: str, include_symbols):
    char_map = "es"
    char_map += "sym" if include_symbols else ""
    decoder = Decoder(source=source, char_map=char_map, direction="tm")
    return decoder.get_result()


def from_morse_to_plain_text(source: dict):
    decoder = Decoder(source=source, char_map="to_plain", direction="mt")
    return decoder.get_result()
