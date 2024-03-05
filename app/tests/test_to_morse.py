from morsedecoder.decoder import Decoder


def get_decoder_result(source):
    decoder = Decoder(source, direction="tm").get_result().get("translated")
    return decoder



class TestClass:

    def test_one(self):
        assert get_decoder_result("hello") == {
            "word1": {
                "char1": "....",
                "char2": ".",
                "char3": ".-..",
                "char4": ".-..",
                "char5": "---"
            }
        }
    
    def test_two(self):
        assert get_decoder_result("hello, world") == {
            "word1": {
                "char1": "....",
                "char2": ".",
                "char3": ".-..",
                "char4": ".-..",
                "char5": "---"
            },
            "word2": {
                "char1": ".--",
                "char2": "---",
                "char3": ".-.",
                "char4": ".-..",
                "char5": "-.."
            }
        }
    
    def test_three(self):
        assert get_decoder_result("1234") == {
            "word1": {
                "char1": ".----",
                "char2": "..---",
                "char3": "...--",
                "char4": "....-"
            }
        }
    
    def test_four(self):
        assert get_decoder_result('"/)/&##&//&(/&/&%#$"$&$/&)=!"/(#)"(#&))') == {
            "word1": {}
        }
    
    def test_five(self):
        assert get_decoder_result("                    ") == {
            "word1": {}
        }
    
    def test_six(self):
        assert get_decoder_result("h/()\"\"&!()e&!$\"ll/&%\"!$\"#o") == {
            "word1": {
                "char1": "....",
                "char2": ".",
                "char3": ".-..",
                "char4": ".-..",
                "char5": "---"
            }
        }