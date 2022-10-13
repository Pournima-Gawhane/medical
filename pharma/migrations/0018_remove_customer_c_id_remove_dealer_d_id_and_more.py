# Generated by Django 4.0.6 on 2022-10-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0017_auto_20171111_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='c_id',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='p_id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phn_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='phn_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phn_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='phn_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='qty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='total',
            field=models.IntegerField(),
        ),
    ]
