from datetime import datetime

def get_angles():
    now = datetime.now()

    seconds = now.second
    minutes = now.minute

    # 360° / 60 = 6° per unit
    sec_angle = seconds * 6
    min_angle = minutes * 6

    return sec_angle, min_angle