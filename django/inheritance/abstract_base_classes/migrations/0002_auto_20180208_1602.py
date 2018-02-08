# Generated by Django 2.0.2 on 2018-02-08 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_base_classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='childb',
            name='other',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_base_classes_childb_set', related_query_name='abstract_base_classes_childb', to='abstract_base_classes.Other'),
        ),
        migrations.AddField(
            model_name='childa',
            name='other',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abstract_base_classes_childa_set', related_query_name='abstract_base_classes_childa', to='abstract_base_classes.Other'),
        ),
    ]
