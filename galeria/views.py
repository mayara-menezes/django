from django.shortcuts import render
# from galeria.models import Album

# foto = Album()
# foto.nome = "Nebulosa de Carina"
# foto.legenda = "Nebulosa de Carina"
# foto.descricao = "A Nebulosa de Carina é uma grande nebulosa de emissão localizada na constelação de Carina. A nebulosa contém várias estrelas de Wolf-Rayet, que são estrelas massivas na fase final de suas vidas. A nebulosa é um dos maiores berçários de estrelas da Via Láctea."
# foto.foto = "carina-nebula.png"
# foto.save()

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')