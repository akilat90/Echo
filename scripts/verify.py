import argparse
from subprocess import run
from subprocess import CalledProcessError
import sys


def main(check):
    try:
        print("Verifying with " + str(check))
        if "flake8" in check:
            print("Linter (flake8)", flush=True)
            run("flake8 -v", shell=True, check=True)
            print("flake8 checks passed")

        if "black" in check:
            print("Formatter (black)", flush=True)
            run("black -v --check .", shell=True, check=True)

    except CalledProcessError:
        sys.exit(1)


if __name__ == "__main__":
    checks = ["flake8", "black"]
    parser = argparse.ArgumentParser()
    parser.add_argument("--checks", default=checks, nargs="+", choices=checks)

    args = parser.parse_args()

    main(args.checks)
