def study_schedule(permanence_period, target_time):
    students_present = 0

    for check_in, check_out in permanence_period:
        try:
            if check_in <= target_time <= check_out:
                students_present += 1
        except TypeError:
            return None

    return students_present
