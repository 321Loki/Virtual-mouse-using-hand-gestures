import numpy as np


def clamp(value, min_value, max_value):
    """Clamp a value between min and max."""
    return max(min(value, max_value), min_value)


def scale_point(value, left_min, left_max, right_min, right_max):
    """Scale a value from one range to another using linear interpolation."""
    return np.interp(value, [left_min, left_max], [right_min, right_max])


def get_angle(a, b, c):
    """
    Returns the angle (in degrees) at point b, formed by points a-b-c.
    Each point should be an (x, y) tuple/list.
    """
    angle1 = np.arctan2(c[1] - b[1], c[0] - b[0])
    angle2 = np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(angle1 - angle2))
    return angle


def get_distance(landmark_list):
    """
    Returns the distance between two landmark points,
    scaled (interpolated) from the 0-1 normalized range to a 0-1000 range.
    """
    if len(landmark_list) < 2:
        return

    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]
    L = np.hypot(x2 - x1, y2 - y1)
    return np.interp(L, [0, 1], [0, 1000])
