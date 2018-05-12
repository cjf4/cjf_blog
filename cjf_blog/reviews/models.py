from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.urls import reverse



class Review(models.Model):
	pub_date = models.DateTimeField('publication date')
	score = models.DecimalField(max_digits = 3, decimal_places=1, blank=True)
	review_title = models.CharField(max_length = 100)
	review_summary = models.CharField(max_length = 50)
	category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
	subject = models.ForeignKey('Subject', null=True, on_delete=models.SET_NULL)
	review_markdown = MarkdownxField(default = 'Post not written yet...')

	@property
	def formatted_markdown(self):
		return markdownify(self.review_markdown)

	def __str__(self):
		return self.review_title

	def get_absolute_url(self):
		return reverse('review-detail', args = [self.id])


	class Meta:
		ordering = ["-pub_date"]

class Category(models.Model):
	category = models.CharField(max_length = 30)

	def __str__(self):
		return self.category 

class Subject(models.Model):
	subject = models.CharField(max_length = 30)

	def __str__(self):
		return self.subject
