from django.shortcuts import render, redirect
from .models import Categoria, Flashcard
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    
    if request.method == "GET":
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcards = Flashcard.objects.filter(user=request.user)

        categoria_filtrar = request.GET.get('categoria')
        dificuldade_filtrar = request.GET.get('dificuldade')

        if categoria_filtrar:
            # Filter by category
            flashcards = flashcards.filter(categoria__id = categoria_filtrar)

        if dificuldade_filtrar:
            # Filter by difficulty
            flashcards = flashcards.filter(dificuldade = dificuldade_filtrar)

        return render(request, 'novo_flashcard.html', {'categorias': categorias, 
                                                       'dificuldades': dificuldades,
                                                       'flashcards': flashcards})
    elif request.method == "POST":
        # Handle form submission
        pergunta = request.POST['pergunta']
        resposta = request.POST['resposta']
        categoria = request.POST['categoria']
        dificuldade = request.POST['dificuldade']

        if len(pergunta.strip()) == 0 or len(resposta) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/flashcard/novo_flashcard/')
        
        flashcard = Flashcard(
            user = request.user,
            pergunta = pergunta,
            resposta = resposta,
            categoria_id = categoria,
            dificuldade = dificuldade,
        )

        flashcard.save()

        messages.add_message(request, constants.SUCCESS, 'Flashcard criado com sucesso')
        return redirect('/flashcard/novo_flashcard')
        
def deletar_flashcard(request, id):
    flashcard = Flashcard.objects.get(id=id)
    flashcard.delete()
    messages.add_message(request, constants.SUCCESS, 'Flashcard deletado com sucesso')
    return redirect('/flashcard/novo_flashcard')