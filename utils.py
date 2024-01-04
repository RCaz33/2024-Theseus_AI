def chunk_text (text):
    tokens_len = 0
    chunks_len = 0
    chunk_n = []
    chunks = []

    for sent in doc.split('.'):
        tokens_len = len(enc.encode(sent))
        if len(enc.encode(sent)) + chunks_len < 500:
            chunks_len += tokens_len
            chunk_n.append(sent)
        else:
            chunks.append('.'.join(chunk_n))
            chunk_n = []
    return chunks


