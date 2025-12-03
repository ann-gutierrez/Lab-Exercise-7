from datetime import datetime


def save_reflection(filename,text):
    if not text or not text.strip():
        raise ValueError('reflection cannot be empty')

    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{timestamp} {text.strip()}\n")

            return True

    except PermissionError:
        raise PermissionError(f"Permission Denied: Cannot write to {filename}")
    except Exception as e:
        raise Exception(f"Error saving reflection: {str(e)}")

