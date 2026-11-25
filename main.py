import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

JOKE = "I hit reply-all to tell everyone to stop replying-all, and now I'm the reason we have a policy."


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
