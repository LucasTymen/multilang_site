# Generated by Django 4.2.13 on 2024-06-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_article_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_question', models.TextField()),
                ('chatbot_response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]