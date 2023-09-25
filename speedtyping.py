import random
import time

# List of random words for the typing test
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

def get_random_word():
    return random.choice(words)

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    # Set the duration of the typing test (in seconds)
    test_duration = 30
    
    end_time = time.time() + test_duration

    word_count = 0
    correct_count = 0

    while time.time() < end_time:
        target_word = get_random_word()
        print(f"\nType this word: {target_word}")
        
        user_input = input("Your input: ")
        
        if user_input == target_word:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect. The correct word was '{target_word}'.")
        
        word_count += 1

    print("\nTest complete!")
    print(f"Words typed: {word_count}")
    print(f"Correct words: {correct_count}")
    print(f"Typing speed: {correct_count / test_duration * 60} words per minute")

if __name__ == "__main__":
    main()
