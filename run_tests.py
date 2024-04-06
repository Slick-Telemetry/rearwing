# Built-in
import os
import subprocess
import sys


# Set the environment variable
os.environ["ENVIRONMENT"] = "TEST"

command = ["pytest", "-rpPfE", "tests"]

# Run the command
result = subprocess.run(command)
sys.exit(result.returncode)
