import time

def stopwatch():
    print("Press Enter to start stopwatch...")
    input()
    starting_time = time.time()

    print("Stopwatch started! Press Enter again to stop...")
    input()
    ending_time = time.time()

    final_time = ending_time - starting_time

    print(f"Final Time: {final_time:.2f}")

stopwatch()
