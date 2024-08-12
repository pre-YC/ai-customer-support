#querying.py
from manage_embedding import load_index
import logging
import sys

async def data_querying(input_text: str):
    """loads index from data directory, queries index with input_text,
    and returns response text from index

    Args:
        input_text (str): user query

    Returns:
        str: response_text from index
    """
    # Load index
    index = await load_index("data")
    engine = index.as_query_engine()

    # queries the index with the input text
    response = engine.query(input_text)
    response_text = response.response
    logging.info(response_text)
    return response_text


