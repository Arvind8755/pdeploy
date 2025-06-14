# Generated by Django 5.0.2 on 2025-06-14 04:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifiapp1', '0005_alter_job_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('keywords', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, help_text='Open Graph image for social sharing', null=True, upload_to='og_images/')),
                ('image_alt', models.CharField(blank=True, help_text='Alternate text for OG Image (used in og:image:alt)', max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_date', models.CharField(blank=True, max_length=100, null=True)),
                ('vacancy_info', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('online_application_date', models.CharField(blank=True, max_length=400, null=True)),
                ('online_last_date', models.CharField(blank=True, max_length=100, null=True)),
                ('receipt_of_application', models.CharField(blank=True, max_length=100, null=True)),
                ('last_date_fee', models.CharField(blank=True, max_length=100, null=True)),
                ('correction_date', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date1', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date2', models.CharField(blank=True, max_length=100, null=True)),
                ('exam_date3', models.CharField(blank=True, max_length=100, null=True)),
                ('admit_card_available', models.CharField(blank=True, max_length=100, null=True)),
                ('answerkey_available_date', models.CharField(blank=True, max_length=100, null=True)),
                ('result_available', models.CharField(blank=True, max_length=100, null=True)),
                ('final_result_available', models.CharField(blank=True, max_length=100, null=True)),
                ('applecation_fee', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('vacancy_details', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('eligibility_criteria', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('selection_process', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('important_information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('how_to_apply', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('apply_online_link', models.URLField(blank=True, null=True)),
                ('admitcard_link', models.URLField(blank=True, null=True)),
                ('answerkeyI_link', models.URLField(blank=True, null=True)),
                ('answerkeyII_link', models.URLField(blank=True, null=True)),
                ('result_link', models.URLField(blank=True, null=True)),
                ('resultI_link', models.URLField(blank=True, null=True)),
                ('resultII_link', models.URLField(blank=True, null=True)),
                ('result_final_link', models.URLField(blank=True, null=True)),
                ('notification_link', models.URLField(blank=True, null=True)),
                ('officialwebsite_link', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='admitcard',
            name='admission_date',
        ),
        migrations.RemoveField(
            model_name='answerkey',
            name='admission_date',
        ),
        migrations.RemoveField(
            model_name='syllabus',
            name='admission_date',
        ),
        migrations.AddField(
            model_name='admitcard',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='admit_card_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='admitcard_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='answerkeyII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='answerkeyI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='answerkey_available_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='applecation_fee',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='apply_online_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='correction_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='eligibility_criteria',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_date1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_date2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='exam_date3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='final_result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='how_to_apply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='image',
            field=models.ImageField(blank=True, help_text='Open Graph image for social sharing', null=True, upload_to='og_images/'),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alternate text for OG Image (used in og:image:alt)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='important_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='keywords',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='last_date_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='notification_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='officialwebsite_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='online_application_date',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='online_last_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='post_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='receipt_of_application',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='resultII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='resultI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='result_final_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='result_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='selection_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='vacancy_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admitcard',
            name='vacancy_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='admit_card_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='admitcard_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='answerkeyII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='answerkeyI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='answerkey_available_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='applecation_fee',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='apply_online_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='correction_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='eligibility_criteria',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='exam_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='exam_date1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='exam_date2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='exam_date3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='final_result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='how_to_apply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='image',
            field=models.ImageField(blank=True, help_text='Open Graph image for social sharing', null=True, upload_to='og_images/'),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alternate text for OG Image (used in og:image:alt)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='important_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='keywords',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='last_date_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='notification_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='officialwebsite_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='online_application_date',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='online_last_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='post_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='receipt_of_application',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='resultII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='resultI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='result_final_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='result_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='selection_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='vacancy_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerkey',
            name='vacancy_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='admit_card_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='admitcard_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='answerkeyII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='answerkeyI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='answerkey_available_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='applecation_fee',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='apply_online_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='correction_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='eligibility_criteria',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_date1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_date2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='exam_date3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='final_result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='how_to_apply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='image',
            field=models.ImageField(blank=True, help_text='Open Graph image for social sharing', null=True, upload_to='og_images/'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alternate text for OG Image (used in og:image:alt)', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='important_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='keywords',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='last_date_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='notification_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='officialwebsite_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='online_application_date',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='online_last_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='post_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='receipt_of_application',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='resultII_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='resultI_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='result_available',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='result_final_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='result_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='selection_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='vacancy_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='vacancy_info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='admitcard',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='answerkey',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='how_to_apply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='important_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='selection_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='vacancy_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='how_to_apply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='important_information',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='selection_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='vacancy_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='title',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
