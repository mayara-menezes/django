from django.db import models

# a classe é um model pq ela representa o banco de dados de dentro do django #

class Album(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    
    # O campo legenda poderia ter sido definido como TextField, porém é mais recomendado que seja usado o CharField pq o número de caracteres é limitado e não há necessidade de um campo de texto #
    legenda = models.CharField(max_length=150, null=False, blank=False)
    
    # O campo descricao é opcional
    descricao = models.TextField(null=False, blank=False)
    
    # O campo data_criacao é preenchido automaticamente com a data e hora
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # como deveria ser, porém utilizando o site de admin do django#
    #foto = models.ImageField(upload_to='media', null=False, blank=False)

    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
# para que possamos rodar a classe criada, é necessário que seja digitado o comando python manage.py makemigrations galeria #

# o comando makemigrations mostra para o django, que temos uma nova tabela de dados para ser criada no banco de dados #

# depois de criado o arquivo de migração, é necessário rodar o comando python manage.py migrate galeria para que a/as funções criadas sejam de fato, migradas #

### como salvar os dados no banco de dados? ###

# no arquivo galeria/views.py, importar o Album: from galeria.models import Album #
# depois, criar uma variável album: album = Album() #
# depois, preencher os campos: album.nome = 'Nome do album' #
# depois, salvar: album.save() #

# para ver os dados salvos, é necessário abrir o shell do django: python manage.py shell #
# depois, importar o Album: from galeria.models import Album #
# depois, listar os dados: Album.objects.all() #
# para ver os dados de um album específico: Album.objects.get(id=1) #
# para deletar um album: album = Album.objects.get(id=1) #
# depois: album.delete() #
# para editar um album: album = Album.objects.get(id=1) #
# depois: album.nome = 'Novo nome' #
# depois: album.save() #
