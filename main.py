import display

def main():
    try:
        display.launchGUI()
    except KeyboardInterrupt:
        #After inputing ctrl+c, click on the GUI for it to receive the shutdown signal
        print("\nReceived KeyBoardInterrupt signal")
        print("Performing graceful shutdown...")

    return 0

if __name__ == "__main__":
    main()