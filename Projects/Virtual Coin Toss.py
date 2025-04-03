import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def main():
    print("Welcome to Virtual Coin Toss CLI App!")
    print("Type 'flip' to toss a coin, 'multi [number]' for multiple tosses, 'stats' for statistics, or 'exit' to quit.")
    
    tosses = []
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "flip":
            result = coin_toss()
            tosses.append(result)
            print(f"Result: {result}")
        elif user_input.startswith("multi"):
            try:
                count = int(user_input.split()[1])
                results = [coin_toss() for _ in range(count)]
                tosses.extend(results)
                print(f"Results: {' '.join(results)}")
            except (IndexError, ValueError):
                print("Please provide a valid number after 'multi'.")
        elif user_input == "stats":
            heads_count = tosses.count("Heads")
            tails_count = tosses.count("Tails")
            print(f"Total Tosses: {len(tosses)}, Heads: {heads_count}, Tails: {tails_count}")
        elif user_input == "exit":
            print("Thanks for using the app! Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()