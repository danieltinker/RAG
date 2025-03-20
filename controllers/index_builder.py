import logging
from utils.tiktoken_truncate_text import truncate_text

class IndexBuilder:
    """
    Builds an index of code snippets with their embeddings. Supports batching to
    reduce API calls.
    """
    def __init__(self, embedding_service, batch_size=100):
        self.embedding_service = embedding_service
        self.batch_size = batch_size

    def build_index(self, symbols):
        index = []
        total_symbols = len(symbols)
        for i in range(0, total_symbols, self.batch_size):
            batch = symbols[i:i+self.batch_size]
            # Filter out symbols with empty or None snippets.
            valid_symbols = [s for s in batch if s.get('snippet') and s['snippet'].strip()]
            if not valid_symbols:
                continue
            # Truncate each snippet to a safe token limit.
            snippets = [truncate_text(s['snippet']) for s in valid_symbols]
            try:
                embeddings = self.embedding_service.get_embeddings_batch(snippets)
            except Exception as e:
                logging.error(f"Error embedding batch starting at index {i}: {e}")
                continue
            for j, symbol in enumerate(valid_symbols):
                entry = {
                    'type': symbol.get('type', 'Unknown'),
                    'name': symbol['name'],
                    'snippet': truncate_text(symbol['snippet']),
                    'file': symbol['file'],
                    'embedding': embeddings[j]
                }
                index.append(entry)
            logging.info(f"Embedded {min(i+self.batch_size, total_symbols)}/{total_symbols} code snippets.")
        return index
