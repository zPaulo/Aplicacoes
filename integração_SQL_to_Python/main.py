from database import db,Usuario,Anuncio

db.connect()
db.create_tables ([Usuario,Anuncio])

# Criando Usuários

Usuario = Usuario.create(nome='Paulo', email='teste@teste.com', senha='123456')
Usuario = Usuario.create(nome='Sara', email='Sara@teste.com', senha='123456')
Usuario = Usuario.create(nome='Joao', email='Joao@teste.com', senha='123456')
Usuario = Usuario.create(nome='Maria', email='Maria@teste.com', senha='123456')

print("Novo Usuário:", Usuario.id, Usuario.nome, Usuario.email)

# Fazendo o SELECT do SQL dentro do python

lista_usuarios = Usuario.select()
print("listando usuários: ")

for u in lista_usuarios:
    print('-', u.id, u.nome, u.email)

# Agora aplicando o WHERE

joao = Usuario.get(Usuario.email == "Joao@teste.com")
print("Usuário: ", joao.id, joao.nome, joao.email, joao.senha)

# Utilizando a função UPDATE

maria = Usuario.get(Usuario.email == "Maria@teste.com")
print("Nome antigo de Maria:", maria.nome)
maria.nome = "Maria Python"
maria.save
print("Maria atualizada:", maria.nome)

# Agora verificando se O sistema permite e-mail duplicado

try:
    usuario_duplicado = Usuario.create(nome = 'Duplicado', email = 'Paulo@teste.com', senha="12345")
except:
    print("Email existente")

# Agora removendo um usuário

usuario_deletado = Usuario.get( Usuario.email == "teste@teste.com")
usuario_deletado.delete_instance()

# Testando um SELECT especificando um usuário deletado

try:
    Usuario.get( Usuario.email == "teste@teste.com")
except:
    print("Usuário deletado")

# Agora criando um novo campo na tabela Anuncio com a chave estrangeira da tabela Usuario

maria = Usuario.get( Usuario.email == "Maria@teste.com")

anuncio = Anuncio.create(
    usuario = maria,
    titulo = "Publicação de Banco de dados",
    descricao = "O projeto seria criar uma publicação de banco de dados e ORM com Python",
    valor = 500.0
)

print("Novo anuncio:", anuncio.id, anuncio.titulo)

# Agora criando outros novos Anuncios com a chave estrangeira da tabela Usuario

Anuncio.create(usuario = maria, titulo = "Anuncio 1", descricao = "Comenta aí", valor = 1000)
Anuncio.create(usuario = maria, titulo = "Anuncio 2", descricao = "Curte aí", valor = 5000)
Anuncio.create(usuario = maria, titulo = "Anuncio 3", descricao = "Compartilha aí", valor = 10000)

# Criando um loop para mostrar todos os anúncios que foram feitos por Maria

print("Anuncios Maria:")
anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "Maria@teste.com")
for a in anuncios_maria:
    print("-", a.id, a.titulo, a.valor)

# Deletando todos os anúncios

Anuncio.delete().execute()

print("Quantidade de anuncios:", Anuncio.select().count())