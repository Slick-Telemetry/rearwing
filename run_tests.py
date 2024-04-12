# Built-in
import argparse
import os
import subprocess
import sys


# Set the environment variable
os.environ["ENVIRONMENT"] = "TEST"

# Setup argument parser
parser = argparse.ArgumentParser(description="Run pytest with optional snapshot update.")
parser.add_argument("--update", action="store_true", help="Include this flag to run with --snapshot-update")

# Parse arguments
args = parser.parse_args()

# Determine command based on --update flag
if args.update:
    command = ["pytest", "--snapshot-update"]
else:
    command = ["pytest", "-rpPfE", "tests"]

# Run the command
result = subprocess.run(command)
sys.exit(result.returncode)
