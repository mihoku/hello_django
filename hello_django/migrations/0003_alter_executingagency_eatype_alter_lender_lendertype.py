# Generated by Django 4.0.3 on 2022-03-27 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django', '0002_eatype_lendertype_executingagency_eatype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executingagency',
            name='EAType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_django.eatype'),
        ),
        migrations.AlterField(
            model_name='lender',
            name='LenderType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_django.lendertype'),
        ),
    ]
