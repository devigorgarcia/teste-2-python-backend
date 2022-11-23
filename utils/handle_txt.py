def read_txt(path):
    list = []
    with open(path, "r", encoding="utf8") as file:
        for line in file:
            list.append(line)
        return list


def split_transactions(transaction: str):
    type = transaction[0:1]
    date = transaction[1:9]
    value = transaction[9:19]
    cpf = transaction[19:30]
    card = transaction[30:42]
    time = transaction[42:48]
    shop_owner = transaction[48:62]
    shop_name = transaction[62:79]
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    # time and date treatment
    full_year = f"{year}/{month}/{day}"
    hour = time[0:2]
    minutes = time[2:4]
    seconds = time[4:6]
    full_hour = f"{hour}:{minutes}:{seconds}"

    # type treatment
    if type == "1":
        type = "Débito"
    elif type == "2":
        type = "Boleto"
    elif type == "3":
        type = "Financiamento"
    elif type == "4":
        type = "Crédito"
    elif type == "5":
        type = "Recebimento Empréstimo"
    elif type == "6":
        type = "Vendas"
    elif type == "7":
        type = "Recebimento TED"
    elif type == "8":
        type = "Recebimento DOC"
    elif type == "9":
        type = "Aluguel"

    split = {
        "type": type,
        "date": full_year,
        "value": int(value),
        "cpf": cpf,
        "card": card,
        "hour": full_hour,
        "shop_owner": shop_owner.rstrip(),
        "shop_name": shop_name.rstrip(),
    }
    return split


def transaction_list(path):
    files = read_txt(path)
    transaction_list = []
    for file in files:
        transaction = split_transactions(file)
        transaction_list.append(transaction)

    return transaction_list
