import markovify

# Load the text corpus
with open("text_corpus.txt", "r") as file:
    text = file.read()

# Create the Markovify model
text_model = markovify.Text(text)

generated_sentence = text_model.make_sentence()
print(generated_sentence)

generated_paragraph = text_model.make_short_sentence(140)
print(generated_paragraph)
