def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if chunk_size <= overlap:
        raise ValueError("Error: chunk size need bigger than overlap")
    if chunk_size <= 0:
        raise ValueError("Error: chuck size <= 0")
    chunks = []
    step = chunk_size - overlap
    if len(tokens) == 0:
        return []
    if len(tokens) <= chunk_size:
        return [tokens]
    for i in range(0, len(tokens), step):
        chunk = tokens[i: i + chunk_size]
        if len(chunk) == chunk_size:
            chunks.append(chunk)
    return chunks