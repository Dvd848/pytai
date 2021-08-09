import argparse
from pytai.application import Application

def main() -> None:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    app = Application()
    
    app.run()


if __name__ == "__main__":
    main()