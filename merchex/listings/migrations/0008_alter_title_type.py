# Generated by Django 4.0.5 on 2022-06-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_title_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('Records', 'Disques'), ('Clothing', 'Vetement'), ('Posters', 'Affiche'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=20),
        ),
    ]