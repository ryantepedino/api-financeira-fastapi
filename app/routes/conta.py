from fastapi import APIRouter
from app.services import conta_service
from app.models.conta_models import Operacao

router = APIRouter()


@router.get("/saldo")
def ver_saldo():
    return conta_service.ver_saldo()


@router.post("/depositar")
def depositar(operacao: Operacao):
    return conta_service.depositar(operacao.valor)


@router.post("/sacar")
def sacar(operacao: Operacao):
    return conta_service.sacar(operacao.valor)

@router.get("/historico")
def historico():
    return conta_service.ver_historico()