from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url   = models.URLField('URL', unique=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)




    def __str__(self):
        return self.title

def __str__(self):
    return self.title

def get_absoulte_url(self): # 현재 데이터의 절대 경로 추출
    return reverse('blog:detail', args=(self.id,))

def get_previous(self): # 이전 데이터 추출
    return self.get_previous_by_modify_dt()

def get_next(self): # 다음 데이터 추출
    return self.get_next_by_modify_dt()