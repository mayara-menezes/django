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

    def __str__(self):
        return self.nome
    
# para que possamos rodar a classe criada, é necessário que seja digitado o comando python manage.py makemigrations galeria #

# o comando makemigrations mostra para o django, que temos uma nova tabela de dados para ser criada no banco de dados #

# depois de criado o arquivo de migração, é necessário rodar o comando python manage.py migrate galeria para que a/as funções criadas sejam de fato, migradas #