def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if chunk_size <= overlap:
        raise ValueError("Error: chunk size need bigger than overlap")
    if chunk_size <= 0:
        raise ValueError("Error: chuck size <= 0")
    len_tokens = len(tokens)
    if len_tokens <= chunk_size:
        return [] if len_tokens == 0 else [tokens]
    chunks = []
    step = chunk_size - overlap
    chunks = [
        tokens[i: i + chunk_size] 
        for i in range(0, len_tokens, step) 
        if len(tokens[i: i + chunk_size]) == chunk_size
    ]
    return chunks