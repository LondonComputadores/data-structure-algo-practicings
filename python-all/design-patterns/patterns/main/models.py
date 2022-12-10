from django.db import models


# V3

class BookManager(models.Manager):

    def starts_with_a(self):
        return super().get_queryset().filter(title__istartswith='a')


class Postable(models.Model):
    title = models.CharField(max_length=200)
    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(Postable):
    word_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title


    objects = BookManager()


class Post(Postable):
    body = models.TextField()


# V2

# class BookManager(models.Manager):

#     def starts_with_a(self):
#         return super().get_queryset().filter(title__istartswith='a')


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     word_count = models.PositiveIntegerField()
#     published_on = models.DateTimeField()
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


#     objects = BookManager()


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     published_on = models.DateTimeField()
#     modified = models.DateTimeField(auto_now=True)


# V1

# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     word_count = models.PositiveIntegerField()
#     published_on = models.DateTimeField()
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    