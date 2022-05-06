from django.db import models


# Create your models here.


class Districts(models.Model):
    dist_name = models.CharField(max_length=120, unique=True)
    population = models.PositiveIntegerField()
    firstdosevr = models.PositiveIntegerField()
    seconddosevr = models.PositiveIntegerField()

    def _str_(self):
        return self.dist_name

# ORM queries
# CRUD
#
# C>>Create

# refname=Modelname(field_name=value,field_name=value,,,,,,)
# refname.save()
# dist=Districts(dist_name="Idukki",population=1000000,firstdosevr=500,seconddosevr=700)
# dist.save()

# R>>Retrieve
# Select all books from our model
# dist=Districts.objects.all()
# dist

# print the details of Idukki district.
# dist=Districts.objects.get(id=1)


# print the details of the districts whoose population is less than 1100000
#dist=Districts.objects.filter(population__lt=1100000)
# dist

# print the details of the districts whoose first dose of vaccine is less than 500
# dist=Districts.objects.filter(firstdosevr__lt=500)
# dist


# Update
# update the population of kollam to 1400000
#dist=Districts.objects.get(id=4)
# dist
# <Districts: Districts object (4)
#  dist.population
# 900000
#  dist.population=1400000
#  dist.save()


# update the name of the district ernakulam to kochi

# dist=Districts.objects.get(id=5)
# dist
# Districts: Districts object (5)
# dist.dist_name
# 'Kochi'
# dist.dist_name="ernakulam"
#  dist.save()


#  Aggregate function


# eg:max,min,average e.t.c
# we need to import these aggregate functions
# from django.db.models import Avg,Sum,Count,Max,Min

# find the highest population from the districts
# dist_popmax=Districts.objects.all().aggregate(Max("population"))
# dist_popmax


# find the highest vaccination rate
# dist_popmax=Districts.objects.all().aggregate(Max("firstdosevr"))


# find the lowest vaccination rate
#dist_popmin=Districts.objects.all().aggregate(Min("firstdosevr"))





