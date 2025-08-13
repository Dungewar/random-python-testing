import random
import json
import os

# Word list with definitions
WORDS = {
    "Innocuous": "Not harmful or offensive.",
    "Paucity": "The presence of something in only small or insufficient quantities; scarcity.",
    "Profusion": "An abundance or large quantity of something.",
    "Versimilitude": "The appearance of being true or real.",
    "Buttress": "A projecting support of stone or brick built against a wall; to support or strengthen.",
    "Corollary": "A proposition that follows from (and is often appended to) one already proved; a natural consequence.",
    "Surmised": "Supposed something is true without having evidence to confirm it.",
    "Stymie": "To prevent or hinder the progress of something.",
    "Disparage": "To regard or represent as being of little worth.",
    "Outstrip": "To move faster than and overtake someone or something.",
    "Putatively": "Generally considered or reputed to be.",
    "Paradigm": "A typical example or pattern of something; a model.",
    "Precariousness": "The state of being dangerously insecure or unstable.",
    "Exactitude": "The quality of being precise or accurate.",
    "Inconspicuousness": "The quality of not being clearly visible or attracting attention.",
    "Anthrology": "The study of flowers and flowering plants. (Note: uncommon word, sometimes confused with 'Anthology' or 'Anthropology'.)",
    "Antecedent": "A thing or event that existed before or logically precedes another.",
    "Prudently": "Acting with or showing care and thought for the future.",
    "Cordially": "In a warm and friendly way.",
    "Rearing": "Bringing up and caring for a child or young animal.",
    "Tentative": "Not certain or fixed; provisional; done without confidence.",
    "Ameliorate": "To make something better or more tolerable.",
    "Postulate": "To suggest or assume the existence, fact, or truth of something as a basis for reasoning.",
    "Evinced": "Revealed the presence of a quality or feeling; indicated clearly.",
    "Contempt": "The feeling that a person or thing is beneath consideration, worthless, or deserving scorn.",
    "Pragmatic": "Dealing with things sensibly and realistically in a way that is based on practical considerations.",
    "Latent": "Existing but not yet developed or manifest; hidden or concealed.",
    "Operative": "Functioning or having effect; a worker, especially a skilled one.",
    "Peripheral": "Relating to or situated on the edge or periphery of something; secondary.",
    "Discresion": "(Likely intended as 'Discretion') The quality of behaving or speaking in such a way as to avoid causing offense or revealing private information.",
    "Preclude": "To prevent from happening; make impossible.",
    "Conspicuous": "Clearly visible; attracting notice or attention.",
    "Lauded": "Highly praised or admired.",
    "Misanthropic": "Having or showing a dislike of humankind and avoiding human society.",
    "Recalcitrant": "Having an obstinately uncooperative attitude toward authority or discipline.",
    "Repudiation": "Rejection of a proposal or idea; refusal to accept.",
    "Tenuous": "Very weak or slight.",
    "Intelligible": "Able to be understood; comprehensible.",
    "Sanguine": "Optimistic or positive, especially in an apparently bad or difficult situation.",
    "Obscurity": "The state of being unknown, inconspicuous, or unimportant."
}

# File to store the scores
SCORES_FILE = "word_scores.json"

# Load existing scores or initialize them
if os.path.exists(SCORES_FILE):
    with open(SCORES_FILE, "r") as f:
        scores = json.load(f)
else:
    scores = {word: 0 for word in WORDS}

def choose_word():
    """Choose a random word from those with the lowest 'gotten right' count."""
    min_score = min(scores.values())
    candidates = [word for word, score in scores.items() if score == min_score]
    return random.choice(candidates)

def main():
    print("Vocabulary Trainer")
    try:
        while True:
            word = choose_word()
            input(f"\n\nYour word: {word}\n(Press Enter when ready to see the definition) ")

            print(f"Definition: {WORDS[word]}")

            correct = input("Did you get it correct? (y/n): ").strip().lower()
            if correct == "y":
                scores[word] += 1
                print(f"Great! '{word}' score is now {scores[word]}")
            else:
                print(f"Okay, '{word}' remains at {scores[word]}")

            # Save updated scores
            with open(SCORES_FILE, "w") as f:
                json.dump(scores, f, indent=2)
    except KeyboardInterrupt:
        print("\n\nBye!")

if __name__ == "__main__":
    main()
