from django import forms
from typing import Any, Optional

class QuizForm(forms.Form):
    """
    A custom Django form class for rendering and processing quiz forms.

    The form dynamically creates a field for each question in the given quiz.
    Each question is presented as a radio button group, allowing users to
    select one answer per question.

    Attributes:
        quiz: A list of quiz questions.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the QuizForm with the given quiz questions.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        # Extract the quiz from the keyword arguments, if provided.
        quiz = kwargs.pop('quiz', None)
        super().__init__(*args, **kwargs)

        # If a quiz is provided, create a form field for each question.
        if quiz is not None:
            for index, question in enumerate(quiz):
                field_name = f'answer_{index}'
                self.fields[field_name] = forms.ChoiceField(
                    choices=question.get_choices(),
                    widget=forms.RadioSelect,
                    label=question.question
                )