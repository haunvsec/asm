# Generated by Django 3.2.4 on 2022-04-06 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targetApp', '0002_auto_20220406_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('creation_date', models.CharField(blank=True, max_length=20, null=True)),
                ('registrar', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='registrantinfo',
            name='associated_domains',
            field=models.ManyToManyField(to='targetApp.AssociatedDomain'),
        ),
    ]
