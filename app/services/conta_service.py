historico = []
saldo = 0


def depositar(valor: float):
    global saldo
    saldo += valor

    historico.append({
        "tipo": "deposito",
        "valor": valor
    })

    return {
        "mensagem": "Depósito realizado com sucesso",
        "saldo": saldo
    }


def sacar(valor: float):
    global saldo

    if valor <= saldo:
        saldo -= valor

        historico.append({
            "tipo": "saque",
            "valor": valor
        })

        return {
            "mensagem": "Saque realizado com sucesso",
            "saldo": saldo
        }
    else:
        return {
            "mensagem": "Saldo insuficiente",
            "saldo": saldo
        }


def ver_saldo():
    return {
        "mensagem": "Saldo atual",
        "saldo": saldo
    }

def ver_historico():
    return {
        "historico": historico
    }

