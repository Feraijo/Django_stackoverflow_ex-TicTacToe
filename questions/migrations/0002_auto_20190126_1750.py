# Generated by Django 2.1.5 on 2019-01-26 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='date answered',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(blank=True),
        ),
    ]