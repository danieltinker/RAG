import tiktoken

def truncate_text(text, max_tokens=2000, encoding_name="cl100k_base"):
    """
    Truncate the text to a maximum number of tokens using tiktoken.
    """
    enc = tiktoken.get_encoding(encoding_name)
    tokens = enc.encode(text)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
        text = enc.decode(tokens)
    return text