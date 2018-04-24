# Generated by Django 2.0.4 on 2018-04-21 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.IntegerField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menuId', models.IntegerField(primary_key=True, serialize=False)),
                ('menuName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pdate', models.DateField(default='01-01-2018')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.Menu'),
        ),
    ]
