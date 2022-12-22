from django.db import connection
from django.db.models.functions import Extract, Concat
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Count, DateTimeField, ExpressionWrapper, Value, CharField, Sum

from .models import Choice, Question, TimeChoice
from django.db.models import Case, When, Q

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

#TODO udělat databázi kde bude datum (zaokrouhleno na minuty) a ve sloupcích bude odpověď, v každé bu%nde počet hlasů
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get(self, request, *args, **kwargs):
        self.request = request  # store the request object
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['res'] = self.request.session.get('res')  # retrieve 'res' from the session
        return context


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Increment the vote count for the selected choice
        selected_choice.votes += 1
        selected_choice.save()
        # Save the time of the vote
        vote_time = timezone.now().strftime("%H:%M")

        # Check if a TimeChoice object with the same time and choice already exists
        # Check if a TimeChoice object with the same time and choice already exists
        time_choice = TimeChoice.objects.filter(
            time=vote_time,
            choice=selected_choice,
        ).first()

        # If the TimeChoice object already exists, increment the vote count
        if time_choice:
            time_choice.vote_count += 1
            time_choice.save()
        else:
            time_choice = TimeChoice.objects.create(
                time=vote_time,
                choice=selected_choice,
                vote_count=1,
            )
        time_choice.save()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM time_votes")
            res = cursor.fetchall()
            print(res)
        request.session['res'] = res

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



