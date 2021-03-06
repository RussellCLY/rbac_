# Generated by Django 3.1.5 on 2021-01-20 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AlterModelOptions(
            name='user2role',
            options={'verbose_name_plural': '用户分配角色表'},
        ),
        migrations.RemoveField(
            model_name='permission2action',
            name='a',
        ),
        migrations.AddField(
            model_name='permission2action',
            name='a',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.action'),
        ),
        migrations.RemoveField(
            model_name='permission2action',
            name='p',
        ),
        migrations.AddField(
            model_name='permission2action',
            name='p',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.permission'),
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='p2a',
        ),
        migrations.AddField(
            model_name='permission2action2role',
            name='p2a',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.permission2action'),
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='r',
        ),
        migrations.AddField(
            model_name='permission2action2role',
            name='r',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.role'),
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='r',
        ),
        migrations.AddField(
            model_name='user2role',
            name='r',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.role'),
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='u',
        ),
        migrations.AddField(
            model_name='user2role',
            name='u',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rbac.user'),
        ),
    ]
