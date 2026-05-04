import read_data
import sorting_algorithms


def parcoursup(data, program_id, capacity, scholarship_quota=0.1):
    pool = [c for c in data if c['program_id'] == program_id]

    # Sort in reverse priority order (sorting_algorithms.merge_sort is stable)
    sorted_pool = sorting_algorithms.merge_sort(pool, 'candidate_id')        # 4. last tiebreaker
    sorted_pool = sorting_algorithms.merge_sort(sorted_pool, 'timestamp')    # 3. earlier timestamp wins
    sorted_pool = sorting_algorithms.merge_sort(sorted_pool, 'is_scholarship') # 2. boursiers first
    sorted_pool = sorting_algorithms.merge_sort(sorted_pool, 'score')        # 1. main criterion
    sorted_pool = sorted_pool[::-1]                       # descending (higher = better)

    # Scholarship reserved spots
    n_scholarship = max(1, int(capacity * scholarship_quota))
    scholars = [c for c in sorted_pool if c['is_scholarship'] == '1']
    non_scholars = [c for c in sorted_pool if c['is_scholarship'] == '0']

    admitted_scholars = scholars[:n_scholarship]
    seen = {c['candidate_id'] for c in admitted_scholars}

    remaining_capacity = capacity - len(admitted_scholars)
    rest = [c for c in sorted_pool if c['candidate_id'] not in seen][:remaining_capacity]

    return admitted_scholars + rest


def display_results(data, capacity=30, scholarship_quota=0.1):
    if data is None:
        print('Error: could not read the CSV file.')
        return

    program_ids = list({c['program_id'] for c in data})  # unique program_ids

    for program_id in program_ids:
        admitted = parcoursup(data, program_id, capacity, scholarship_quota)

        print(f'=== Parcoursup Results — Program {program_id} ===')
        print(f'Capacity: {capacity} | Scholarship quota: {int(scholarship_quota * 100)}%\n')

        for rank, candidate in enumerate(admitted, start=1):
            scholar_tag = '[Boursier]' if candidate['is_scholarship'] == '1' else ''
            print(f'{rank}. Candidate {candidate["candidate_id"]} '
                  f'| Score: {candidate["score"]} '
                  f'| Timestamp: {candidate["timestamp"]} '
                  f'| HS: {candidate["hs_id"]} '
                  f'{scholar_tag}')
        print()  # blank line between programs
