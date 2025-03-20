# utils/formatter.py

def print_formatted_function_console(func_name, func_text, language="cpp"):
    """
    Prints the function name and its content to the terminal using Rich.
    """
    from rich.console import Console
    from rich.syntax import Syntax
    console = Console()
    console.rule(f"[bold green]{func_name}[/bold green]")
    syntax = Syntax(func_text, language, theme="monokai", line_numbers=True)
    console.print(syntax)

def print_formatted_function_streamlit(func_name, func_text, language="cpp"):
    """
    Displays the function name and its content in a Streamlit app.
    """
    import streamlit as st
    st.header(func_name)
    st.code(func_text, language=language)