# Generated by Django 4.2.1 on 2024-08-28 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paitent', '0003_alter_paitent_age_alter_paitent_user'),
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_review',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='paitent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='paitent.paitent'),
        ),
    ]
