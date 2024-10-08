from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=30, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateField(verbose_name='생성날짜', auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    # def get_absolute_url(self):
    #     return f'/notice/{self.pk}/'
    
    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'


class Image(models.Model):
    notice = models.ForeignKey(Notice, related_name='image', on_delete=models.CASCADE)
    image = models.ImageField('이미지', upload_to='image/%Y/%m/%d')
    uploaded_at = models.DateTimeField(verbose_name='업로드날짜', auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} for {self.notice.title}"

    class Meta:
        verbose_name = "삽입이미지"
        verbose_name_plural = "삽입이미지"
