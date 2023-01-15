# SheHacks+7: "Speak-Easy"
## Inspiration
Language is one of the core components to expression, communication, and culture. The internet provides so many new opportunities for individuals to learn a new language. But online discussions can be slow, online courses can be boring, and translators aren't quite as accurate as true native speaking.

Through our passion for education, culture, and community, we wanted to find a better way to speak like a native: whether you are visiting a new country, learning deeper vocabulary, or are just curious about the different dialects of our diverse world. By utilizing a user-friendly interface, Cohere's NLP langauge models, and a community discussion forum, Speak-Easy grants the ease, efficiency, and accessibility for users to learn a new language.

## What it does
- Using Cohere's AI-generated content writer, Users have the option to receive suggestions of different ways of saying their translated phrase so they are not just stuck with the dictionary translation: by establishing the context of the formality of their phrase (informal/formal), users get suggestions that are appropiate to their situation. This is a great way to learn slang, common phrases, proper grammar, and more.
- Speak-Easy hosts an online forum for users to share ideas, ask questions, and help each other out.
- A dictionary feature that allows users to save their favourite phrases and words.

## How we built it
- For the translation suggestion functionality, we used Cohere's AI-generated content writer, providing examples of what is considered "formal" and "informal" language in the English language.
- We created the community post system using a class system in Python, with a PostManager to record posts in a dictionary database of our application.

## Challenges we ran into
- Accessing Google's Translation API: Frequently encountered an AttributeError when trying to translate foreign phrases. May be an issue with the Google Translation API itself?
- We decided to have replies not repliable, to simplify our database.

## Accomplishments that we're proud of
- Experimenting with AI for the first time.
- Completing [some of] our first hackathons!
- Being able to find a solution to our problem.
- Completing each of our different roles of our project.

## What we learned
- More of how AI/ML learns and operates, along with how to integrate the benefits of AI into projects to help create a solution.
- The complexities behind creating applications and their features, even something as simple as we see everyday, like posting online or creating an internet profile.
- How much can be completed in about 36 hours!

## What's next for Speak-Easy
- Create a language translation that works for both ways -- not just into English. As AI language models become more complex, we hope for comapnies like Cohere to expand internationally to spread our mission (and hopefully we can contribute to that initiative!)
- An educational feature along with our translations to help users learn more about international cultures:
  - i.e.: "Americans commonly use *abbreviations* in their text slang, such as 'Laugh Out Load' to 'LOL'. Some people even extend this language to their verbal speech!"
- Create a log-in/log-out system for Users to save their personalized profiles, posts, favourited phrases, etc.
- Give translations that adhere to different emotions as well.
- Real-time conversations with real-life people who are online, or AI chat robots (possibly by using Cohere's chat generization/summarization models)

