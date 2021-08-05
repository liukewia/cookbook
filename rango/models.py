from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class FavouriteRecipe(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self


class Recipe(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    LONG_CONTENT_MAX_LENGTH = 2083
    SHORT_CONTENT_MAX_LENGHT = 500

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    favouriteRecipe = models.ManyToManyField(FavouriteRecipe)
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    likes = models.IntegerField(default=0)
    ingredients = models.CharField(max_length=SHORT_CONTENT_MAX_LENGHT)
    directions = models.CharField(max_length=LONG_CONTENT_MAX_LENGTH)
    url = models.URLField(max_length=URL_MAX_LENGTH, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    CONTENT_MAX_LENGTH = 256

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField(max_length=CONTENT_MAX_LENGTH)

    def __str__(self):
        return f'{self.recipe.title}_{self.user_profile.user.username}'





