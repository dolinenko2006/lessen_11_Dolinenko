import json

def get_candidates_from_json():
    """
    загрузит данные из файла
    :return: список result_json из candidates.json
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        result_json = json.load(file)
        return result_json

def get_candidates():
    """
    выводит всех кандидатов
    :return: выведет все что есть в json файле
    """
    return get_candidates_from_json()

def get_by_pk(pk):
    """
    вернет кандидата по pk
    :param pk: порядковый номер
    :return: имя кандидата
    """
    for candidate in get_candidates():
        if pk == candidate["pk"]:
            return candidate
    return

def get_by_skill(skill):
    """
    вернет кандидатов по навыку
    :param skill: навык "go, python"
    :return: список кандидатов (именна)
    """
    candidates_with_skill = []
    for candidate in get_candidates():
        if skill.lower() in candidate["skills"].lower().split(", "):
            candidates_with_skill.append(candidate)
    return candidates_with_skill


def get_candidates_by_name(candidate_name):
    """
    выводит кандидата по имени
    :param candidate_name: имя кандидата или часть его имени
    :return:
    """
    candidates_with_name = []
    for candidate in get_candidates():
        if candidate_name.lower() in candidate["name"].lower():    ##.split(", "):
            candidates_with_name.append(candidate)
    return candidates_with_name
