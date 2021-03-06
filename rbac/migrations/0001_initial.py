# Generated by Django 3.1.5 on 2021-01-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='动作')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=64, verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='Permission2Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.ManyToManyField(to='rbac.Action', verbose_name='动作')),
                ('p', models.ManyToManyField(to='rbac.Permission', verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='角色')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名称')),
                ('password', models.CharField(max_length=64, verbose_name='用户密码')),
            ],
        ),
        migrations.CreateModel(
            name='User2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r', models.ManyToManyField(to='rbac.Role', verbose_name='角色')),
                ('u', models.ManyToManyField(to='rbac.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Permission2Action2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p2a', models.ManyToManyField(to='rbac.Permission2Action', verbose_name='具体权限')),
                ('r', models.ManyToManyField(to='rbac.Role', verbose_name='角色')),
            ],
        ),
    ]
