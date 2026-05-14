# 💰 API Financeira com FastAPI

API simples para gerenciamento de saldo com operações de depósito, saque e histórico de transações.

---

## 🚀 Tecnologias utilizadas

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

---

## 📌 Funcionalidades

- ✔ Depositar valores
- ✔ Sacar valores com validação de saldo
- ✔ Consultar saldo atual
- ✔ Histórico de transações

---

## 📂 Estrutura do projeto
app/
├── routes/
│ └── conta.py
├── services/
│ └── conta_service.py
├── models/
│ └── conta_models.py
main.py


---

## ▶️ Como rodar o projeto

```bash
git clone https://github.com/ryantepedino/api-financeira-fastapi.git
cd api-financeira-fastapi
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --reload

🌐 Acesse a documentação
http://127.0.0.1:8000/docs
💡 Sobre o projeto

Este projeto foi desenvolvido com foco em prática de desenvolvimento backend com FastAPI, aplicando conceitos de:

Separação de responsabilidades (routes, services, models)
Validação de dados com Pydantic
Estruturação de APIs REST
👨‍💻 Autor

Ryan Tepedino
📍 Juiz de Fora - MG
🔗 https://github.com/ryantepedino
