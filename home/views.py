from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
import random

# Create your views here.

def home(request):
    return HttpResponse("Hello From Django")

def get_quiz(request):
    try:
        # Converting to list to use shuffle on it
        question_objs = list(Question.objects.all())
        data = []

        #random.shuffle(question_objs)
        for question_obj in question_objs:
            #print(question_obj.get_answers())
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })

        payload = {'status': True, 'data' : data}


        return JsonResponse(payload)

    except Exception as e:
            print(e)
    return HttpResponse("Somethings Wrong")