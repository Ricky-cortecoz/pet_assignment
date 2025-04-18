from pet import Pet

def main():
    # Create your digital pet
    Bllody = Pet("Bllody")

    # Initial status
    Bllody.get_status()

    # Feed, play, and rest
    Bllody.eat()
    Bllody.play()
    Bllody.sleep()

    # Train some tricks
    Bllody.train("roll over")
    Bllody.train("play dead")

    # Show learned tricks
    Bllody.show_tricks()

    # Final status
    Bllody.get_status()

if __name__ == "__main__":
    main()