# Generated by Django 4.2.6 on 2023-11-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postlist', '0004_postlist_delete_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Postlist',
        ),
    ]
