from django.shortcuts import render, redirect
from .models import Categoria, Flashcard, FlashcardDesafio, Desafio
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
    
    if request.user.is_authenticated:
        # Check if flashcard belongs to user
        flashcard = Flashcard.objects.filter(id=id, user=request.user).first()

        if flashcard:
            flashcard.delete()
            messages.add_message(request, constants.SUCCESS, 'Flashcard deletado com sucesso')
        else:
            messages.add_message(request, constants.ERROR, 'Flashcard não encontrado ou não pertence ao usuário')

        return redirect('/flashcard/novo_flashcard')
    
def iniciar_desafio(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        return render(request, 'iniciar_desafio.html', {'categorias': categorias, 
                                                        'dificuldades': dificuldades})
    elif request.method == "POST":
        # Handle form submission
        titulo = request.POST.get('titulo')
        categoria = request.POST.getlist('categoria')
        quantidade_perguntas = request.POST.get('quantidade_perguntas')
        dificuldade = request.POST.get('dificuldade')

        desafio = Desafio(
            user = request.user,
            titulo = titulo,
            quantidade_perguntas = quantidade_perguntas,
            dificuldade = dificuldade,
        )

        desafio.save()

        desafio.categoria.add(*categoria)

        flashcards = (
            Flashcard.objects.filter(user=request.user)
            .filter(dificuldade=dificuldade)
            .filter(categoria_id__in=categoria)
            .order_by('?')
        )

        if flashcards.count() < int(quantidade_perguntas):
            messages.add_message(request, constants.ERROR, 'Não há flashcards suficientes para o desafio')
            return redirect('/flashcard/iniciar_desafio')
        
        flashcards = flashcards[:int(quantidade_perguntas)]

        for f in flashcards:
            flashcard_desafio = FlashcardDesafio(
                flashcard = f
            )
            flashcard_desafio.save()
            desafio.flashcards.add(flashcard_desafio)
        
        desafio.save()
