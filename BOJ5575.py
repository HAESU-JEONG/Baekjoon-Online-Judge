for _ in range(3):
    h_start, m_start, s_start, h_end, m_end, s_end = map(int, input().split())

    start_time = h_start * 3600 + m_start * 60 + s_start
    end_time = h_end * 3600 + m_end * 60 + s_end

    time_result = end_time - start_time

    hour = time_result // 3600
    time_result -= 3600 * hour
    minute = time_result // 60
    time_result -= 60 * minute
    sec = time_result

    print(hour, minute, sec)