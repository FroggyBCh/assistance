from django.db import models

# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True, blank=True)
#
# class PowerUser(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

class Problem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True,default='')
    owner = models.ForeignKey("auth.User", related_name='problems', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    class Meta:
        ordering = ["created"]
    def __str__(self):
        return self.title

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey("auth.User", related_name="comments", on_delete=models.CASCADE)
    problem = models.ForeignKey("Problem", related_name="comments", on_delete=models.CASCADE)
    class Meta:
        ordering = ["created"]