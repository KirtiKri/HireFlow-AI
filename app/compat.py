"""Small Streamlit compatibility helpers.

Newer Streamlit releases replace ``use_container_width=True`` with
``width="stretch"``. ``stretch(fn)`` returns whichever keyword the installed
version supports, so the UI works across Streamlit 1.35+.
"""
import inspect


def stretch(fn) -> dict:
    """Keyword arguments that make a Streamlit element fill its container."""
    try:
        params = inspect.signature(fn).parameters
    except (TypeError, ValueError):
        return {}
    if "use_container_width" in params:
        return {"use_container_width": True}
    if "width" in params:
        return {"width": "stretch"}
    return {}
