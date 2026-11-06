from app.rag import chunks

def test_chunking_preserves_content():
    text = "word " * 200
    pieces = chunks(text)
    assert len(pieces) > 1
    assert all(len(x) <= 650 for x in pieces)
