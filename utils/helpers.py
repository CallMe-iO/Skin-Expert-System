def validate_input(text):
    if not text.strip():
        raise ValueError("Input tidak boleh kosong")
    return True