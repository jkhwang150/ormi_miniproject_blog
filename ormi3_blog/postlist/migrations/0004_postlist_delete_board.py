# Generated by Django 4.2.6 on 2023-11-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postlist', '0003_board_delete_postlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
