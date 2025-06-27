from repositories.config import get_db_connection
from repositories.usuario_repository_interface import UsuarioRepositoryInterface
from models.usuario import Usuario

class UsuarioMySQLRepository(UsuarioRepositoryInterface):
    def create(self, usuario: Usuario):
        sql = "INSERT INTO usuarios (id, nome, email, senha) VALUES (%s, %s, %s, %s)"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (usuario.id, usuario.nome, usuario.email, usuario.senha))
            conn.commit()
        except Exception as e:
            print(f"Error creating user: {e}")

    def find(self, usuario_id: str):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql, usuario_id)
            result = cursor.fetchone()
            if result:
                return Usuario(id=result['id'], nome=result['nome'], email=result['email'], senha=result['senha'])
            return None
        except Exception as e:
            print(f"Error finding user: {e}")
            return None
        
    def update(self, usuario: Usuario):
        sql = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.id))
            conn.commit()
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete(self, usuario_id: str):
        sql = "DELETE FROM usuarios WHERE id = %s"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql, usuario_id)
            conn.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")

    def find_all(self):
        sql = "SELECT * FROM usuarios"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            return [Usuario(id=row['id'], nome=row['nome'], email=row['email'], senha=row['senha']) for row in results]
        except Exception as e:
            print(f"Error finding all users: {e}")
            return []
        
    def find_by_email(self, email: str):
        sql = "SELECT * FROM usuarios WHERE email = %s"
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            if result:
                return Usuario(id=result['id'], nome=result['nome'], email=result['email'], senha=result['senha'])
            return None
        except Exception as e:
            print(f"Error finding user by email: {e}")
            return None
