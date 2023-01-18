from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Video
from .forms import VideoForm
import random
da1 = [["media/bounty.mp4", "Bounty", "Bucket", "Ballot", "Bleed", "Belief"], ["media/book.mp4", "Book", "Brook", "Block", "BLack", "Broom"], ["media/mice.mp4", "Mice", "Mark", "Meet", "Major", "Man"], ["media/boot.mp4", "Boot", "Beet", "Meet", "Heat", "Beak"], ["media/heat.mp4", "Hoot", "Heat", "Him", "Heat", "Heal"], ["media/pool.mp4",
                                                                                                                                                                                                                                                                                                                                  "pool", "pull", "poke", "pain", "peel"], ["media/soap.mp4", "soup", "soap", "soake", "sell", "seat"], ["media/see.mp4", "see", "seep", "sold", "sour", "seek"], ["media/jeep.mp4", "joke", "leap", "jake", "jam", "jeep"], ["media/soup.mp4", "soap", "soake", "sold", "sour", "seek"], ["media/leap.mp4", "jeep", "leap", "lake", "late", "look"]]
questions = random.sample(da1, 4)
questions_result = []
question_num = 0
score = 0


def index(request):
    global questions
    questions = random.sample(da1, 4)
    if request.method == 'GET':
        return render(request, 'index.html', {'data': 1})


def quiz(request):
    global question_num, score, questions_result

    if question_num == 0:
        questions_result = []
        score = 0

    questions_result.append(
        [questions[question_num][0], questions[question_num][0][len("media/"):-4]])

    if request.method == 'GET':
        return render(request, 'quiz.html', {'data': questions[question_num]+[score]})

    elif request.method == 'POST':
        # get variable from post request
        # save to database
        current_answer = questions[question_num][0][len("media/"):-4]
        question_num += 1
        selected_answer = request.POST.get('option').lower()
        if current_answer == selected_answer:
            score += 1

        if question_num == 4:
            question_num = 0
            return render(request, 'result.html', {'data': questions_result+[score]})

        return render(request, 'quiz.html', {'data': questions[question_num]+[score]})
