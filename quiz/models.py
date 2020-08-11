from django.db import models

# Create your models here.

class Question(models.Model):
	Content=models.CharField(max_length=150)
	Option1=models.CharField(max_length=150)
	Option2=models.CharField(max_length=150)
	Option3=models.CharField(max_length=150)
	Option4=models.CharField(max_length=150)



class PoliticalViews(Question):
	Ans1=models.CharField(max_length=150)
	Ans2=models.CharField(max_length=150)
	Ans3=models.CharField(max_length=150)
	Ans4=models.CharField(max_length=150)
	
	def __str__(self):
		return self.Content

class IQTest(Question):
	Correct=models.CharField(max_length=150)
	
	def __str__(self):
		return self.Content

class FastFood(Question):
	Ans1=models.CharField(max_length=150)
	Ans2=models.CharField(max_length=150)
	Ans3=models.CharField(max_length=150)
	Ans4=models.CharField(max_length=150)

	def __str__(self):
		return self.Content