from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
# def index(request):
#     latest_question_list=Question.objects.order_by("-pub_date")[:5]
#     context={"latest_question_list":latest_question_list}
#     return render(request,'vote/index.html',context)

# def detail(request,question_id):
#     try:
#         question=Question.objects.get(id=question_id)

#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
    
#     return render(request,'vote/detail.html',{"question":question})



# def detail1(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,"vote/detail.html",{"question":question})






# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "vote/results.html", {"question": question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(
            request,
            "vote/detail.html",
            {
                "question":question,
                "error_message":"No choice selected",
            }
        )
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('vote:results',args=(question.id,)))





class IndexView(generic.ListView):
    template_name = "vote/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "vote/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "vote/results.html"
