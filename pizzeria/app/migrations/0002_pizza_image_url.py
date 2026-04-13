from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='image_url',
            field=models.URLField(blank=True, verbose_name='Фото (URL)'),
        ),
    ]
