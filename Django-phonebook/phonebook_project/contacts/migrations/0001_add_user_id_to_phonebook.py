
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),  # Replace XXXX with the previous migration number
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='user',
            field=models.ForeignKey(to='auth.User', on_delete=models.CASCADE),
        ),
    ]