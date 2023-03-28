from django.db import models

# Create your models here.
class TodoList(models.Model):
    listName = models.CharField(max_length=30, blank=False, null=False)

    def _str_(self) -> str:
        return "listName={}".format(self.listName)

class ListItem(models.Model):
    itemDescription = models.CharField(max_length=1000, blank=False, null=False)
    complete = models.BooleanField(default=False)
    listFk = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return "{} - {}".format(self.complete, self.itemDescription)