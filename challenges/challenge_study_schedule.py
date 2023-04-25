def study_schedule(permanence_period: list[tuple], target_time: int):
    try:
        result_count = 0
        for period in permanence_period:
            if (period[0] <= target_time <= period[1]):
                result_count += 1

        return result_count
    except TypeError:
        return None
