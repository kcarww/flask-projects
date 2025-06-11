from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.models import Base  # Assumindo que os models estão em um arquivo chamado models.py

# Configuração da conexão com MySQL
# Formato: mysql+pymysql://usuario:senha@host:porta/nome_do_banco
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/sistema_os"

# Criar engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Para ver os SQLs executados (remover em produção)
    pool_pre_ping=True  # Verifica conexão antes de usar
)

# Criar SessionLocal para interações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    """Cria todas as tabelas no banco de dados"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")

def get_db():
    """Função para obter sessão do banco"""
    db = SessionLocal()
    return db

if __name__ == "__main__":
    # Criar as tabelas
    create_tables()