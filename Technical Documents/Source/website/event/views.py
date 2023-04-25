from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from logins.models import Player
from .forms import QuizForm
from django.contrib import messages


@login_required
def quiz(request, event_id: int):
    """
    View function for the quiz page to handle the players' quiz attempts

    :param request: The incoming HTTP request
    :param event_id: The ID of the associated event
    """
    # Retrieve the event and related quiz
    event = Event.objects.get(pk=event_id)
    quiz = event.questionSet.all()

    # Retrieve the current player, create a new one if it doesn't exist
    player, created = Player.objects.get_or_create(user=request.user)

    # Check if the player has already attempted this event
    if player.attempted_events.filter(pk=event_id).exists():
        messages.warning(request, 'You have already attempted this event.')
        return redirect('home')

    # Process the submitted form
    if request.method == 'POST':
        form = QuizForm(request.POST, quiz=quiz)
        if form.is_valid():
            # Extract user answers and correct answers
            user_answers = [form.cleaned_data[f'answer_{i}'] for i in range(len(quiz))]
            correct_answers = [question.answer for question in quiz]

            # Check if the user's answers are correct
            if user_answers == correct_answers:
                trash_item = event.trashId
                player.add_trash_item(trash_item)
                player.add_points(trash_item.value)
                player.attempted_events.add(event)
                player.save()

                messages.success(request, 'You answered correctly! The trash item has been added to your bin.')
                return redirect('home')
            else:
                # Show an error message if the user answered incorrectly
                context = {'form': form, 'event': event, 'quiz': quiz, 'error': 'You answered incorrectly. Please try again.'}
                return render(request, 'quiz.html', context)

    # Render the quiz page with an empty form
    form = QuizForm(quiz=quiz)
    context = {'form': form, 'event': event, 'quiz': quiz}
    return render(request, 'quiz.html', context)