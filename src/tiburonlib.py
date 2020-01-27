from datetime import datetime

def paso_a_fecha(text):
    for fmt in ('%d-%b-%y', '%d-%b-%Y', '%Y.%m.%d'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    return None