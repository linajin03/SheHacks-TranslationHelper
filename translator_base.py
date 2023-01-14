import cohere
from googletrans import Translator

co = cohere.Client('uAAXOvSLigsz9qCYyB0FhfSk7VGPL3pekqhynDfm')


class SpeakEasyTranslator:
    """SpeakEasyTranslator: a class that translates the given input while also
    generating suggestions of other ways to say the phrase depending on the
    desired level of formality.

    === Public Attributes ===
    inputted_phrase: the inputted phrase by the user to translate into English
    """
    inputted_phrase: str

    def __init__(self, inputted_phrase: str) -> None:
        """Initialize the instance variables, where .
        """
        self.inputted_phrase = inputted_phrase

    def translate_phrase(self) -> str:
        """Return the translated phrase of user input"""
        translator = Translator()
        translated_text = translator.translate(self.inputted_phrase)
        return translated_text.text

    def suggest(self, tone: str) -> str:
        """Return different suggestions of the user's input depending on their
        desired context/tone.
        """
        response = co.generate(
            model='xlarge',
            prompt='This is paraphrasing program that generates different ways'
                   'of saying the inputted phrase in different formalities '
                   'according to who the user is talking to.\n--\n'
                   'Phrase: Where are you?\nTone: Informal\n'
                   'Suggestion: where you at\n--\n\nPhrase: I don\'t care.'
                   '\nTone: Formal'
                   '\nSuggestion: This isn\'t a scope of my focus right now'
                   '\n--\n\nPhrase: Oh my god\nTone: Informal\n'
                   'Suggestion: omg\n--\n\nPhrase: omg'
                   '\nTone: Formal\nSuggestion: Oh my goodness.'
                   '\n--\n\nPhrase: ' + self.inputted_phrase +
                   '\nTone: ' + tone + '\nSuggestion:',
            max_tokens=100,
            temperature=0.8,
            k=0,
            p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE')
        return 'Prediction: {}'.format(response.generations[0].text)


if __name__ == "__main__":
    # Example usage:
    user_input = input("Enter your desired phrase to translate: ")
    transl = SpeakEasyTranslator(user_input)
    formality = input("Is this in a formal or informal context? Type 'informal'"
                      " or 'formal': ")
    return_statement = "Another way you can say this is: " + \
                       transl.suggest(formality).replace('-', '')
    print(return_statement)

