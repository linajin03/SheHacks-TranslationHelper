from googletrans import Translator
import cohere
from cohere.classify import Example

# examples = [
#     Example("when r u coming 2day?", "informal"),
#     Example("When are you arriving today?", "formal"),
#     Example("are you coming today", "informal"),
#     Example("What is ur ETA?", "informal"),
#     Example("Could you please be a little more quiet?", "formal"),
#     Example("Shut up", "informal"),
#     Example("I don't care", "informal"),
#     Example("I do not think this something I am focused on right now",
#             "formal"),
#     Example("whats your number", "informal"),
#     Example("Could I have your contact information?", "formal"),
#     Example("Do you have time to talk right now?", "formal"),
#     Example("that's cap", "informal")
# ]

co = cohere.Client('uAAXOvSLigsz9qCYyB0FhfSk7VGPL3pekqhynDfm')


class SpeakEasyTranslator:
    """SpeakEasyTranslator: a class that translates the given input while also
    generating suggestions
    === Public Attributes ===
    inputted_phrase: the inputted phrase by the user to translate
    context: the context provided by the user to give more specific translation
    """
    inputted_phrase: str
    context: str

    def __init__(self, inputted_phrase: str, context: str) -> None:
        """Initialize the instance variables.
        """
        self.inputted_phrase = inputted_phrase
        self.context = context

    def translate(self) -> str:
        """Return the translated phrase of user input"""
        translator = Translator()
        return translator.translate(self.inputted_phrase)

    def suggest(self) -> str:
        """Return different suggestions of the user's input depending on their
        desired context/tone.
        """
        response = co.generate(
            model='xlarge',
            prompt='This is paraphrasing program that generates different ways'
                   'of saying the inputted phrase in different formalities '
                   'according to who the user is talking to.\n--\n'
                   'Phrase: Where are you?'
                   '\nAudience: Friend'
                   '\nSuggestion: where ya at\n--\n'
                   '\nPhrase: I don\'t care.'
                   '\nAudience: Teacher'
                   '\nSuggestion: This isn\'t a part of my focus at the moment'
                   '\nPhrase: ' + self.inputted_phrase +
                   '\nAudience: ' + self.context +
                   '\nSuggestion: ',
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
    pass
