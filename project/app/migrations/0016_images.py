# Generated by Django 3.0.8 on 2020-10-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_post_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage', models.ImageField(default='images/my_background.jpg', upload_to='')),
                ('about_images1', models.ImageField(default='images/basket_ball.jpg', upload_to='')),
                ('about_images2', models.ImageField(default='images/footballball.jpg', upload_to='')),
                ('about_images3', models.ImageField(default='images/military.jpg', upload_to='')),
                ('blog_background_image', models.ImageField(default='images/boxing.jpg', upload_to='')),
                ('contact_background_image', models.ImageField(default='images/boxing.jpg', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
    ]
