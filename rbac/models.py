from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名称')
    password = models.CharField(max_length=64, verbose_name='用户密码')
    # m = models.ManyToManyField('Role')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户表'

class Role(models.Model):
    caption = models.CharField(max_length=32, verbose_name='角色')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = '角色表'

class User2Role(models.Model):
    u = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    r = models.ForeignKey(Role, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.u.username}-{self.r.caption}'

    class Meta:
        verbose_name_plural = '用户分配角色表'

class Action(models.Model):
    caption = models.CharField(max_length=32, verbose_name='操作名')
    code = models.CharField(max_length=32, verbose_name='操作')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = '操作表'

class Menu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self', related_name='p', on_delete=models.CASCADE, default='', null=True,
                               blank=True)

    def __str__(self):
        return f'{self.caption}'

    class Meta:
        verbose_name_plural = '菜单'

class Permission(models.Model):
    caption = models.CharField(max_length=32, verbose_name='权限名')
    url = models.CharField(max_length=64, verbose_name='权限')
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'URL表'

class Permission2Action(models.Model):
    p = models.ForeignKey(Permission, on_delete=models.CASCADE, default='')
    a = models.ForeignKey(Action, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.p.caption}-{self.a.caption} : {self.p.url}?t={self.a.code}'

    class Meta:
        verbose_name_plural = '权限表'

class Permission2Action2Role(models.Model):
    p2a = models.ForeignKey(Permission2Action, on_delete=models.CASCADE, default='')
    r = models.ForeignKey(Role, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.r.caption}-->{self.p2a}'

    class Meta:
        verbose_name_plural = '角色分配权限表'

