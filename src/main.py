import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Lightweight video classifier"
    )
    parser.add_argument("--video", help="Path to input video")
    args = parser.parse_args()

    if args.video:
        parser.error(
            "Video classification is not implemented yet. "
            "Complete the feature extraction and model pipeline first."
        )

    parser.print_help()


if __name__ == "__main__":
    main()
