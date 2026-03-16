def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    stopword_set = {word for word in stopwords}

    filter_token = [token for token in tokens if token not in stopword_set]

    return filter_token