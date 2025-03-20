import clang.cindex
import os
import logging
from config import find_libclang

# Set the library file for Clang.
libclang_path = find_libclang()
if not libclang_path:
    libclang_path = input(
        "libclang not found, please enter path to libclang library(.dll/.so/.dylib):")
clang.cindex.Config.set_library_file(libclang_path)
clang.cindex.Config.set_compatibility_check(False)


def get_cursor_text(cursor: clang.cindex.Cursor):
    """
    Returns the exact text corresponding to the cursor's extent.
    """
    extent = cursor.extent
    file_name = extent.start.file.name
    # Read the file content
    try:
        with open(file_name, 'rb') as f:
            content = f.read()
    # The extent provides offset values into the file content.
    except Exception as e:
        logging.error(f"Error reading {file_name}: {e}")
        return None
    content = content[extent.start.offset:extent.end.offset].decode("utf-8")
    return content

# def get_cursor_text(cursor):
#     """
#     Returns the exact text corresponding to the cursor's extent.
#     """
#     extent = cursor.extent
#     file_name = extent.start.file.name
#     # Read the file content
#     try:
#         with open(file_name, 'r', encoding='utf-8') as f:
#             content = f.read()
#     # The extent provides offset values into the file content.
#     except Exception as e:
#             logging.error(f"Error reading {file_name}: {e}")
        
#     return content[extent.start.offset:extent.end.offset]

def get_functions(source_file):
    """
    Parse the given source file using clang and return a list of tuples.
    Each tuple contains the function name and the full text of the function.
    Works for both C and C++ files.
    """
    # Determine the language standard based on file extension.
    ext = os.path.splitext(source_file)[1]
    if ext == '.c':
        args = ['-std=c11']
    else:
        args = ['-std=c++14']
    
    index = clang.cindex.Index.create()
    translation_unit = index.parse(source_file, args=args)
    
    functions = []
    
    def visitor(cursor, parent):
        # Only process nodes that originate from the source file we are parsing.
        if cursor.location and cursor.location.file:
            if os.path.abspath(cursor.location.file.name) == os.path.abspath(source_file):
                if cursor.kind in (clang.cindex.CursorKind.FUNCTION_DECL, 
                                   clang.cindex.CursorKind.CXX_METHOD):
                    func_name = cursor.spelling
                    func_text = get_cursor_text(cursor)
                    functions.append((func_name, func_text))
        for child in cursor.get_children():
            visitor(child, cursor)
    
    visitor(translation_unit.cursor, None)
    return functions