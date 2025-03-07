import weaviate

client = weaviate.connect_to_local()

questions = client.collections.get("School")

response = questions.generate.near_text(
    query="what is reproduction",
    limit=2,
    grouped_task="you are a teacher and you have to provide information in a paragraph with no boundation of words to use you can use any number if words to make students understand deep knowledge"
)

print(response.generated)  # Inspect the generated text

client.close()  # Free up resources