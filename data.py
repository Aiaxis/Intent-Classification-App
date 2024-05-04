import pandas as pd

# Example intents and their corresponding examples
greet_examples = [
    "Hi", "How are you?", "Hello", "Good morning", "Good evening", 
    "Hey", "Hey there", "What’s up?", "How do you do?", "How's it going?",
    "Good afternoon", "Good night", "Hola", "Bonjour", "Guten Tag", 
    "Ciao", "こんにちは", "안녕하세요", "Welcome back", "Long time no see",
    "Nice to see you again", "Glad to see you", "Hi there", "Hello there",
    "Hiya", "Howdy", "Pleased to meet you", "It’s a pleasure to meet you",
    "I’m delighted to meet you", "What’s new?", "What’s good?", "How’s everything?",
    "How’s your day?", "How’s your day going?", "What’s happening?", "What’s going on?",
    "How have you been?", "How’s life treating you?", "How’s your family?",
    "What’s the good word?", "How’s your day been so far?", "Are you okay?",
    "Is everything alright?", "How’s your morning?", "Good to see you",
    "It’s been a while", "Where have you been hiding?", "Look who it is!",
    "Look what the cat dragged in!", "There you are!", "How’s it hanging?",
    "What’s cooking?", "What’s kicking?", "Hello again", "Greetings", "Salutations",
    "I greet you", "How are you doing today?", "What’s new with you?",
    "How’s your evening?", "How’s the night treating you?", "Welcome", 
    "Good day", "How is everything?", "Anything new?", "All good?",
    "Happy to see you", "Always a pleasure", "Cheers", "Yo", "Sup",
    "Hey buddy", "Hey pal", "Hi friend", "Good to have you here", "You’re welcome",
    "Nice to have you back", "Here’s to seeing you", "I’ve missed you", "We’ve missed you",
    "How’s the family?", "How’s work?", "How’s the job?", "How’s school?", "How’s life?",
    "Greetings and salutations", "Hello my friend", "Hey my friend", "Good to meet you",
    "Happy to meet you", "Welcome aboard", "Glad you’re here", "Nice to meet you too",
    "It’s great to see you", "It’s great to have you here"
]


farewell_examples = [
    "Goodbye", "Bye", "Farewell", "See you", "Later", "Good night", "See you tomorrow",
    "See you later", "See you soon", "Catch you later", "Take it easy", "Take care",
    "Be seeing you", "Stay safe", "Peace out", "Take care of yourself", "I wish you well",
    "I bid you farewell", "Until we meet again", "I’ll miss you", "Sad to see you go",
    "It’s hard to say goodbye", "Don’t be a stranger", "Let’s keep in touch",
    "Looking forward to our next meeting", "Outta here", "I’m off", "Gotta run", "Gotta jet",
    "Adios", "Cheerio", "Goodbye for now", "Bye for now", "Until next time", "See ya",
    "So long", "Goodbye my friend", "Fare thee well", "Hope to see you again soon",
    "Until we meet again", "Adieu", "Bye-bye", "Toodle-oo", "Catch you on the flip side",
    "Time for me to go", "I've got to get going", "It was nice seeing you", "Au revoir",
    "Auf Wiedersehen", "Sayonara", "Hasta la vista", "Goodbye for now", "Take good care",
    "Keep in touch", "Wishing you all the best", "Farewell for now", "Until later", 
    "Have a good one", "Bye for now", "Talk to you soon", "See you next time", 
    "Take care now", "All the best", "I must be going", "Time to hit the road",
    "Have a nice day", "Have a good day", "Farewell my friend", "It’s been real",
    "Catch ya later", "I gotta bounce", "Time to scoot", "Gotta head out",
    "Peace", "See you around", "I’m outta here", "Heading out", "See you in the funny papers",
    "Catch you later alligator", "After a while crocodile", "I'll be seeing you", 
    "Safe travels", "Keep well", "Best wishes", "Bye for now", "See you on the other side",
    "Hope to see you again", "Until then", "Farewell for now", "Take it easy", "Safe journey",
    "I look forward to our next meeting", "Farewell until next time", "See you on the other side"
]

inquiry_examples = [
    "What time is it?", "Can you help me?", "Do you know where my keys are?", "How do I get to the city center?",
    "What’s the weather forecast for tomorrow?", "Who won the game last night?", "When is the next train?",
    "Can I book a table for two?", "Is this item in stock?", "When do you close today?",
    "Where is the nearest ATM?", "How far is the airport?", "Can you direct me to the nearest hospital?",
    "How are you feeling today?", "What are your plans for the weekend?", "What do you think about this book?",
    "What are the main responsibilities of your job?", "Can you explain this report?", "How can we improve our process?",
    "Can you show me how to use this software?", "What are the system requirements?", "How do I reset my password?",
    "What are your hours of operation?", "Where can I find the restroom?", "How much does this cost?",
    "Are there any discounts available?", "What ingredients are in this dish?", "Can I have some water?",
    "Where can I park my car?", "What languages do you speak?", "Do you take credit cards?",
    "How long does delivery take?", "Can I change my order?", "What is your return policy?",
    "How can I contact customer service?", "What is the deadline for this project?", "Who is in charge here?",
    "How do I subscribe to your newsletter?", "Can you recommend a good restaurant nearby?",
    "Where can I buy tickets?", "What are the best sights to see in this city?", "Do you have vegetarian options?",
    "Is there a gym nearby?", "What’s your WiFi password?", "Can you check the stock for me?",
    "How old do you have to be to rent a car?", "What are the side effects of this medication?",
    "Can I see a menu?", "What are the terms of the warranty?", "How many calories are in this?",
    "Can you play some music?", "Where is the closest subway station?", "When was this building constructed?",
    "What’s the exchange rate today?", "Can I get directions to your office?", "What size should I get?",
    "How safe is this neighborhood?", "Can I leave a message?", "Who should I contact for more information?",
    "When is your next appointment available?", "Where did you buy that?", "Can I have a receipt?",
    "What is the local specialty?", "How long have you been in business?", "Can this be customized?",
    "Do you offer gift wrapping?", "Where is this product made?", "How to apply for a refund?",
    "Can I take a brochure?", "Are pets allowed?", "What vegan options do you have?",
    "Is the kitchen still open?", "Can I take photos here?", "Do you have any recommendations for local tours?",
    "Where can I recharge my phone?", "How do I get a taxi?", "What are your best-selling products?",
    "Can I pay in installments?", "What type of oil do you use?", "Can children dine here?",
    "Are you open during holidays?", "What flavors are available?", "Do you have online services?",
    "How frequent are the bus services?", "Can you deliver to my house?", "What forms of ID do you need?",
    "Can you hold this for me?", "Do you have a loyalty program?", "Can I get this in a different color?",
    "How do I use this device?", "What’s the capacity of this hall?", "Can I book a room for tonight?"
]

# Combine into a single dataset
data = []
for example in greet_examples:
    data.append((example, "Greet"))
for example in farewell_examples:
    data.append((example, "Farewell"))
for example in inquiry_examples:
    data.append((example, "Inquiry"))

# Create a DataFrame
df = pd.DataFrame(data, columns=["Text", "Intent"])

# Shuffle the dataset (optional, improves model training)
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
df.to_csv("intent_dataset.csv", index=False)

print("Dataset created and saved to intent_dataset.csv")
