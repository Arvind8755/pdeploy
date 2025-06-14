# Generated by Django 5.0.2 on 2025-06-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifiapp1', '0006_admission_remove_admitcard_admission_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='draft', max_length=100),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='public', max_length=100),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='public', max_length=100),
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='public', max_length=100),
        ),
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='public', max_length=100),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('public', 'Public')], default='draft', max_length=100),
        ),
    ]
