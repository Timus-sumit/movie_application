from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class List(models.Model):
    user= models.ForeignKey(User,related_name='list', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    highlighted = models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b/%e/%y')


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(List, self).save(*args, **kwargs)
