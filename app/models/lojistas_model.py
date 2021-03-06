from app.models.endereco_model import Endereco
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class Lojistas(db.Model):
    id: int
    nome: str
    email: str
    # senha: str
    cnpj: str
    telefone: str
    endereco_id: int

    __tablename__ = "lojistas"

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cnpj = Column(String(14), nullable=False)
    telefone = Column(String(11), nullable=False)
    endereco_id = Column(Integer, ForeignKey("endereco.id"), nullable=True)

    lojista_endereco = relationship("Endereco", backref=backref("endereco_lojista"))

    @property
    def serialized(self):
        data = {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "cnpj": self.cnpj,
        }

        if self.endereco_id:
            endereco = Endereco.query.filter_by(id = self.id).first()
            if endereco:
                data["endereco"] = {
                    "Logradouro": endereco.logradouro,
                    "Numero": endereco.numero,
                    "Bairro": endereco.bairro,
                    "Complemento": endereco.complemento,
                    "Cidade": endereco.cidade,
                    "Estado": endereco.estado,
                    "CEP": endereco.cep
                }
        return data

    @property
    def password(self):
        return {"Error password cannot be accessed"}

    @password.setter
    def password(self, password):
        self.senha = generate_password_hash(password=password, salt_length=10)

    def check_password(self, password_compare):
        return check_password_hash(self.senha, password_compare)
