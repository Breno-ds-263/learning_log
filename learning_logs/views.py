from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required 

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """A página inicial de Learning Log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Mostra todos os tópicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas."""
    topic = get_object_or_404(Topic, id=topic_id)
    # Garante que o assunto pertence ao usuário atual
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um novo tópico"""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova entrada para um tópico específico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco
        form = EntryForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # Cria o objeto sem salvar ainda
            new_entry.topic = topic              # Associa a nova entrada ao tópico
            new_entry.save()                    # Salva a nova entrada no banco de dados
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Requisição incial; prenche previamente o formuário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de POST submetidos; processa os dados
        form = EntryForm(instance=entry ,data=request.POST)
        if form.is_valid():
            form.save()                    # Salva a nova entrada no banco de dados
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry' : entry ,'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


