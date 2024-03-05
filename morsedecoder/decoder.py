from .constants import TO_MORSE, TO_PLAIN_TEXT
from .char_maps import get_char_map
from .utils import clean_accents
from .exceptions import InvalidSourceFormat, BadDirection
import re


class Decoder:
    def __init__(
        self,
        source: str | dict,
        char_map: str,
        direction="mt",
    ) -> None:
        self.__source = source
        self.__normalized_source = (
            clean_accents(source.lower()) if isinstance(source, str) else None
        )
        self.__char_map_repo = get_char_map(char_map)
        self.__word_sep = "_"
        self.__result = None
        self.__direction = direction
        self.__untokenizable = list()
        self.__decode()

    def get_result(self):
        return {
            "tokenized": self.__result,
            "source": self.__source,
            "normalized_source": (
                self.__normalized_source if self.__direction == TO_MORSE else None
            ),
            "untokenized": self.__untokenizable,
            "direction": (
                "from morse to plain text"
                if self.__direction == TO_PLAIN_TEXT
                else "from plain text to morse"
            ),
        }

    def __decode(self):
        if self.__direction not in [TO_MORSE, TO_PLAIN_TEXT]:
            raise BadDirection(f"Invalid direction for {self.__direction}")

        self.__result = (
            self.__to_morse()
            if self.__direction == TO_MORSE
            else self.__to_plain_text()
        )

    def __to_morse(self):
        if self.__normalized_source:
            parsed_source = self.__parse_plain_text(self.__normalized_source)
        else:
            raise InvalidSourceFormat(
                "From text plain to morse the source must be string"
            )

        tokens = self.__char_map_repo.get("char_map")

        words = parsed_source.split(self.__word_sep)
        words = [elem for elem in words if elem != ""]

        result = {}
        for i, word in enumerate(words):
            serie = {
                f"token{n+1}": tokens[word[n]]
                for n in range(len(word))
                if word[n] != "_"
            }
            result.update({f"serie{i + 1}": serie})

        return result

    def __to_plain_text(self):
        if not isinstance(self.__source, dict):
            raise InvalidSourceFormat(
                "From morse to plain text source must be an object"
            )

        result = []
        for codes in self.__source.values():
            word = str()
            if isinstance(codes, dict):
                for char in codes.values():
                    if not isinstance(char, str):
                        continue
                        # raise InvalidSourceFormat(
                        #     "From morse to plain text source must be a 3-level object"
                        # )
                    signal = self.__char_map_repo["char_map"].get(char)
                    if signal:
                        word += signal
                    else:
                        self.__untokenizable.append(char)
                result.append(word)
        return " ".join(result)

    def __parse_plain_text(self, source: str):

        source = source.split(" ")
        source = [elem for elem in source if elem != ""]
        source = self.__word_sep.join(source)

        self.__untokenizable = list(
            set(re.findall(self.__char_map_repo.get("pattern"), source))
        )

        clean_source = re.sub(
            self.__char_map_repo.get("pattern"),
            "",
            source,
        )

        return clean_source
