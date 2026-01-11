import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()


def speak(text):
    """Speak the given text aloud."""
    engine.say(text)
    engine.runAndWait()


def spelling_bee_game():
    print("🦖 Welcome to the Dinosaur Spelling Bee! 🦖")
    print("Listen carefully and spell the dinosaur's name correctly to move to the next level.\n")

    levels = {
        "Easy": ["stego", "trex", "diplo"],
        "Average": ["velociraptor", "pterodactyl", "brachiosaurus"],
        "Difficult": ["ankylosaurus", "allosaurus", "spinosaurus"],
        "Expert": ["micropachycephalosaurus", "iguanodon", "dreadnoughtus"]
    }

    for level, dinosaurs in levels.items():
        print(f"\n--- {level} Level ---")
        for dino in dinosaurs:
            # Speak the dinosaur name
            speak(f"Spell the dinosaur: {dino}")

            while True:
                answer = input("Your spelling: ").lower().replace(" ", "")
                if answer == dino.lower():
                    print("✅ Correct! Well done.\n")
                    speak("Correct! Well done!")
                    break
                else:
                    print("❌ Incorrect! Try again.")
                    speak("Incorrect! Try again.")

    print("🎉 Congratulations! You have completed the Dinosaur Spelling Bee! 🦕")
    speak("Congratulations! You have completed the Dinosaur Spelling Bee!")


# Start the game
if __name__ == "__main__":
    spelling_bee_game()
