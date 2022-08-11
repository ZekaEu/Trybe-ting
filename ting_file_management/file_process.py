import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if path_file in instance.search(i)["nome_do_arquivo"]:
            return None
    file_to_process = txt_importer(path_file)
    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_to_process),
        "linhas_do_arquivo": file_to_process
    }
    instance.enqueue(processed_file)
    print(processed_file)


def remove(instance):
    if not len(instance):
        print("Não há elementos")
    else:
        file_name = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file_name} removido com sucesso")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        print(metadata)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
