# Importa o objeto `db` que representa a conexão com o banco de dados
from db import db

# Define a classe Restaurante como um modelo de dados do SQLAlchemy
class Restaurante(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'restaurantes'

    # Define a estrutura da tabela com suas colunas
    id = db.Column(db.Integer, primary_key=True)  # Coluna ID, chave primária
    nome = db.Column(db.String(100), nullable=False)  # Nome do restaurante, obrigatório
    endereco = db.Column(db.String(200), nullable=False)  # Endereço do restaurante, obrigatório
    tipo_cozinha = db.Column(db.String(100), nullable=False)  # Tipo de cozinha (ex: italiana, japonesa)

    # Método para converter o objeto em formato JSON
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'tipo_cozinha': self.tipo_cozinha
        }