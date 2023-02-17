from django.db import models

class Dept(models.Model):
    deptno=models.IntegerField()
    dname=models.CharField(max_length=30)
    loc=models.CharField(max_length=30)



class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    mgr=models.IntegerField()
    job=models.CharField(max_length=30)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
