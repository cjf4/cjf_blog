from django import forms

class CreateReviewForm(forms.Form):
	score = forms.DecimalField(max_digits = 3, decimal_places=1)
	subject_name = forms.CharField(max_length = 30)
	review_summary = forms.CharField(max_length = 50)
	category = forms.CharField(max_length = 30)
	review_text = forms.CharField(initial = "Write the review here.")

	def clean_score(self):
		score = self.cleaned_data['score']

		if score < 0 or score > 10:
			raise ValidationError('Score must be 0 through 10')

		return score

