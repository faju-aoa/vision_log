from django.shortcuts import render,redirect

from vision_logs.models import Topic
from vision_logs.forms import TopicForm,ContentForm


# Create your views here.

def index(request):

    return render(request, 'vision_logs/base.html', {'study':'study'})

def topics(request):

    topics = Topic.objects.all().order_by('date_added')
    context = {'topics': topics}
    return render(request, 'vision_logs/topics.html', context)

def new_topics(request):
    """Add a new topic."""

    if request.method != 'POST':
         form = TopicForm()
         content_form = ContentForm()
    else:
        form = TopicForm(data=request.POST)
        content_form = ContentForm(data=request.POST)
    if form.is_valid():
        topic = form.save()
        new_content = content_form.save(commit=False)
        new_content.content = topic  # Link content to the newly created topic
        new_content.save()
        return redirect('vision_logs:topics')
    context = {'form': form, 'content_form': content_form}
    return render(request, 'vision_logs/new_topics.html', context)
'''
def new_content(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = ContentForm()
    else:
        form  = ContentForm(data=request.POST)
    if form.is_valid():
        new_content = form.save(commit=False)
        new_content.content = topic
        new_content.save()
        return redirect('vision_logs:topics')
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form }
    return render(request, 'vision_logs/new_topics.html', context)
'''