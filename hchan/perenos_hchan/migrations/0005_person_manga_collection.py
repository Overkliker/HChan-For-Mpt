# Generated by Django 4.2 on 2023-05-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perenos_hchan', '0004_card_delete_manga_delete_person_delete_postavte5_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=300)),
                ('manga_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perenos_hchan.card')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perenos_hchan.card')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perenos_hchan.person')),
            ],
        ),
    ]