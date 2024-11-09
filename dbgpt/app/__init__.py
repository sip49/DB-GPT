"""The app package.

This package will not be uploaded to PyPI. So, your can't import it if some other package depends on it.
"""
import os
import sys

from dotenv import load_dotenv
import secrets

if "pytest" in sys.argv or "pytest" in sys.modules or os.getenv("CI"):
    print("Setting random seed to 42")
    secrets.SystemRandom().seed(42)

# Load the users .env file into environment variables
load_dotenv(verbose=True, override=True)

del load_dotenv
