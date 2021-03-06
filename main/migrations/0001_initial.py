# Generated by Django 3.2.8 on 2022-07-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True, verbose_name="Ma'lumot")),
                ('duration', models.PositiveIntegerField(default=10, verbose_name='Davomiyligi')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='UZS')),
                ('price_usd', models.PositiveIntegerField(default=100, verbose_name='USD')),
                ('image', models.ImageField(upload_to='city_images/')),
                ('leave', models.DateField(blank=True, null=True, verbose_name="Ketish sanasi (To'ldirish shart emas)")),
                ('back_to', models.DateField(blank=True, null=True, verbose_name="Qaytish sanasi (To'ldirish shart emas)")),
            ],
            options={
                'verbose_name': "Yo'nalish",
                'verbose_name_plural': "Yo'nalishlar",
            },
        ),
    ]
