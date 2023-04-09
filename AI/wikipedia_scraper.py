import wikipedia
try:
    # Enter the topic
    topic = input("What you wanna know?")
    # Search for articles about a topic
    results = wikipedia.search(topic)

    # Get the content of the first article
    page = wikipedia.page(results[0])
    content = page.content

    # Print the title and content of the article
    print(page.title)
    print(content)
except wikipedia.exceptions.DisambiguationError as e:
    print("This got way to many articles, choose one from these :")
    for i, option in enumerate(e.options):
        print(f"{i+1}. {option}")
