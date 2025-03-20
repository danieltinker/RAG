# symbol_extractor.py

import os
import logging
from utils.clang_function_parser import get_functions

class SymbolExtractor:
    """
    Extracts various symbols (functions, structs, macros, typedefs, enums,
    constants, and variables) from a C/C++ source file.
    """
    
    def extract_from_code(self, file_path):
        """Extract all symbols from the given code string."""
        symbols = []
        funcs = get_functions(file_path)
        for name, text in funcs:
            symbols.append({
                        'type': 'Function',
                        'name': name,
                        'snippet': text,
                        'file': file_path
                    })
        return symbols
    
    
def extract_symbols_from_directory(dir_path):
    """
    Traverse a directory and extract symbols from all C/C++ files.
    """
    extractor = SymbolExtractor()
    all_symbols = []
    file_count = 0
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(('.c', '.cpp')):
                file_path = os.path.join(root, file)
                logging.info(f"Processing {file_path}...")
                symbols = extractor.extract_from_code(file_path)
                if symbols:
                    all_symbols.extend(symbols)
                file_count += 1
    logging.info(f"Processed {file_count} files in total.")
    return all_symbols