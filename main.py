import wikipedia
import pandas as pd

# topics = ['The Great Pyramid of Giza','Marie_Curie','The Beatles','World War I','Mount Everest','The Roman Empire','The Solar System','The Renaissance','Barack Obama','The Titanic','The Cold War','Ancient Egypt','The Mona Lisa','Winston Churchill','The Human Genome Project','The Great Wall of China','Jane Austen','The Industrial Revolution','The Eiffel Tower','Pablo Picasso','The American Civil War','The Taj Mahal','Albert Einstein','The French Revolution','The Wright Brothers','Leonardo da Vinci','Nelson Mandela','The Panama Canal','The Apollo 11 Mission','The Mayan Civilization','The Black Death','Queen Elizabeth II','The Renaissance','The Amazon Rainforest','The Olympic Games','The Seven Wonders of the Ancient World','The Space Race','The Crusades','The United Nations','The Sistine Chapel','Mahatma Gandhi','The Titanic','William Shakespeare','The Silk Road','The Berlin Wall','The Himalayas','The Mona Lisa','The Great Barrier Reef','The First World War','The Second World War'] # your list of topics
topics = ["History of the Roman Empire","Artificial intelligence","Global warming","The Beatles","World War II","Neuroscience","Greek mythology","Sustainable energy","Human anatomy","African American history","Space exploration","Classical music","Quantum mechanics","Psychology","Cryptocurrency","British monarchy","Genetics","French Revolution","Food and nutrition","Ancient Egypt","Hinduism","American football","Environmentalism","European Union","Architecture","Buddhism","Medieval Europe","Cinema","North American wildlife","World literature","Epidemiology","Artificial neural networks","Industrial revolution","Classical antiquity","International trade","Mathematics","Modern art","Immunology","Marketing","Paleontology","Philosophy","Physics","Renewable energy","Robotics","Software engineering","Tourism","Women's suffrage","Zoology","History of medicine","Climate change adaptation"]


data = []

for topic in topics:
    try:
        page = wikipedia.page(topic)
        print(dir(page)) 
        link = page.url
        data.append([topic, page, link])
    except wikipedia.exceptions.DisambiguationError as e:
        # if there is a disambiguation page for the topic, you can choose one of the options or skip the topic
        print(f"Disambiguation error: {e.options}")
    except wikipedia.exceptions.PageError:
        # if there is no Wikipedia page for the topic, you can skip it
        print(f"No Wikipedia page found for {topic}")

df = pd.DataFrame(data, columns=['Topic', 'Summary', 'Link'])
df.to_excel('wikipedia_data.xlsx', index=False)
