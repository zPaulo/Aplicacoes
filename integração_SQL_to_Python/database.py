from peewee import *

db = SqliteDatabase('freelancers.db')

# Criando banco de dados de Usuários

class Usuario(Model):
    nome = CharField()
    email = CharField(unique = True)
    senha = CharField()

    class Meta:
        database = db

# Criando banco de dados de Anúncios

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref = 'usuarios')
    titulo = CharField()
    descricao =  TextField()
    valor = DecimalField()

    class Meta:
        database = db