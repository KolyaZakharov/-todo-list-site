from django.core.management import call_command
from django.db import migrations


def load_fixtures(state, schema_editor):
    call_command("loaddata", "todo_list_data.json")


def reverse_load_fixtures(state, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_content"),
    ]

    operations = [migrations.RunPython(load_fixtures, reverse_load_fixtures)]
