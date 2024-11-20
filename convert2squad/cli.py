import argparse
from command.convert2squad import convert2squad

def main():
    """
    Main function to parse command-line arguments and execute the convert2squad command.
    """
    parser = argparse.ArgumentParser(
        description="Execute the convert2squad command with required file inputs."
    )

    parser.add_argument(
        "command",
        type=str,
        choices=["convert2squad"],
        help="Command to execute. Supported: 'convert2squad'."
    )
    parser.add_argument(
        "-q", "--question",
        type=str,
        required=True,
        help="File path to the question file."
    )
    parser.add_argument(
        "-a", "--answer",
        type=str,
        required=True,
        help="File path to the answer file."
    )
    parser.add_argument(
        "-c", "--context",
        type=str,
        required=True,
        help="File path to the context file."
    )

    args = parser.parse_args()

    if args.command == "convert2squad":
        convert2squad(args.question, args.answer, args.context)

if __name__ == "__main__":
    main()
