def exists_word(word, instance):
    file = instance.data[0]
    occurrence_list = []
    for i, file_row in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in file_row.lower():
            occurrence_list.append({"linha": i + 1})
    if occurrence_list:
        return [{
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": occurrence_list,
        }]
    else:
        return occurrence_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
