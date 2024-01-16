def solution(participant, completion):
    part_map = dict()
    comp_map = dict()
    for part in participant:
        if part not in part_map:
            part_map[part] = 0
        part_map[part] += 1
  
    for comp in completion:
        if comp not in comp_map:
                comp_map[comp] = 0
        comp_map[comp] += 1

    for part in part_map:
        if part not in comp_map:
            return part
        elif part_map[part] != comp_map[part]:
            return part

    return ''
