from pydantic import BaseModel, Field


class Operacao(BaseModel):
    valor: float = Field(..., gt=0, description="Valor deve ser maior que zero")