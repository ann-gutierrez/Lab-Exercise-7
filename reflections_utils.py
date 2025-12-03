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


def read_reflection(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reflections = [line.strip() for line in file if line.strip()]
            return reflections

    except FileNotFoundError:
        return []
    except PermissionError:
        raise PermissionError(f"Permission Denied: Cannot write to {filename}")
    except Exception as e:
        raise Exception(f"Error reading reflection: {str(e)}")


def search_reflections(keyword, reflections_list):
    if not keyword or not keyword.strip():
        return []

    keyword_lower = keyword.strip().lower()

    matches = [
        reflection for reflection in reflections_list
        if keyword_lower in reflection.lower()
    ]

    return matches