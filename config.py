# config.py

import os
import logging
import sys
from dotenv import load_dotenv

# =============================================================================
# Configuration & Logging Setup
# =============================================================================
def find_libclang():
    # Check if an environment variable is provided for the libclang path.
    env_path = os.environ.get("LIBCLANG_PATH")
    if env_path and os.path.exists(env_path):
        return env_path

    # Determine the OS and set up possible library paths.
    if sys.platform == "darwin":
        # macOS common paths for libclang.dylib
        possible_paths = [
            "/Library/Developer/CommandLineTools/usr/lib/libclang.dylib",
            "/usr/local/opt/llvm/lib/libclang.dylib",
            "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/libclang.dylib"
        ]
    elif sys.platform.startswith("linux"):
        # Linux common paths for libclang.so
        possible_paths = [
            "/usr/lib/llvm-12/lib/libclang.so",
            "/usr/lib/llvm-11/lib/libclang.so",
            "/usr/lib/llvm-10/lib/libclang.so",
            "/usr/lib/x86_64-linux-gnu/libclang-10.so.1",
            "/usr/lib/x86_64-linux-gnu/libclang-11.so.1",
            "/usr/lib/x86_64-linux-gnu/libclang-12.so.1"
        ]
    elif sys.platform == "win32":
        # For Windows, check an optional environment variable first.
        env_win = os.environ.get("LLVM_LIB_DIR")
        if env_win:
            candidate = os.path.join(env_win, "libclang.dll")
            if os.path.isfile(candidate):
                return candidate
        # Fallback to a common install path for LLVM on Windows.
        possible_paths = [
            r"C:\Program Files\LLVM\bin\libclang.dll"
        ]
    else:
        possible_paths = []

    # Return the first valid path found.
    for path in possible_paths:
        if os.path.isfile(path):
            return path

    return None


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# Load variables from .env into the environment
load_dotenv()

# Access the secret from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# API & Model Configuration
EMBEDDING_MODEL = 'text-embedding-3-small'
