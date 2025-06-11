from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    
    matricula = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    loja = Column(String(50), nullable=False)
    senha = Column(String(255), nullable=False)
    tipo = Column(String(20), nullable=False)  # 'consultor' ou 'supervisor'
    
    # Relacionamento com OrdemServico
    ordens_servico = relationship("OrdemServico", back_populates="funcionario")
    
    __mapper_args__ = {
        'polymorphic_identity': 'funcionario',
        'polymorphic_on': tipo
    }

class Consultor(Funcionario):
    __mapper_args__ = {
        'polymorphic_identity': 'consultor'
    }

class Supervisor(Funcionario):
    __mapper_args__ = {
        'polymorphic_identity': 'supervisor'
    }

class OrdemServico(Base):
    __tablename__ = 'ordens_servico'
    
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, default=datetime.utcnow, nullable=False)
    problema = Column(String(500), nullable=False)
    solucao = Column(String(500))
    status = Column(String(20), default='Aberta', nullable=False)
    matricula_funcionario = Column(Integer, ForeignKey('funcionarios.matricula'), nullable=False)
    
    # Relacionamento com Funcionario
    funcionario = relationship("Funcionario", back_populates="ordens_servico")