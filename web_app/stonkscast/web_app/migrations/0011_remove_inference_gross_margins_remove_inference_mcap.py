# Generated by Django 4.1 on 2023-01-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0010_remove_inference_kgv"),
    ]

    operations = [
        migrations.RemoveField(model_name="inference", name="gross_margins",),
        migrations.RemoveField(model_name="inference", name="mcap",),
    ]
