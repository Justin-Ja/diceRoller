import display

def main():
    print("Main file execution goes here")

    try:
        display.launchGUI()
    except KeyboardInterrupt:
        print("\nReceived KeyBoardInterrupt signal")
        print("Performing graceful shutdown...")

    return 0

if __name__ == "__main__":
    main()