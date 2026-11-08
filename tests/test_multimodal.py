from io import BytesIO
from types import SimpleNamespace
import pytest
from app.multimodal import extract_visual_text


def image_bytes():
    from PIL import Image
    out = BytesIO()
    Image.new('RGB', (200, 120), 'white').save(out, 'PNG')
    return out.getvalue()


class FakeCompletions:
    def __init__(self):
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content='Python and SQL'))])


def test_visual_image_uses_mock_vision_model():
    completions = FakeCompletions()
    client = SimpleNamespace(chat=SimpleNamespace(completions=completions))
    result = extract_visual_text('fictional.png', image_bytes(), client=client, model='vision-test')
    assert 'Python and SQL' in result
    assert 'page 1' in result
    assert completions.calls[0]['model'] == 'vision-test'
    assert completions.calls[0]['messages'][1]['content'][1]['type'] == 'image_url'


def test_rejects_unsupported_file():
    with pytest.raises(ValueError, match='supports'):
        extract_visual_text('x.docx', b'fake', client=object(), model='vision-test')


def test_rejects_oversized_file():
    with pytest.raises(ValueError, match='5 MB'):
        extract_visual_text('x.png', b'x' * (5 * 1024 * 1024 + 1), client=object(), model='vision-test')


def test_requires_vision_model(monkeypatch):
    monkeypatch.delenv('VISION_MODEL', raising=False)
    with pytest.raises(ValueError, match='VISION_MODEL'):
        extract_visual_text('x.png', image_bytes(), client=object())
