# Generated by Django 4.0.4 on 2023-12-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_alter_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
