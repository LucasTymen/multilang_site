
**internationalization.md:**
```markdown
# Internationalization

## Création des fichiers de traduction

1. Créez des fichiers de traduction :

    ```sh
    django-admin makemessages -l fr -l it -l de -l es
    ```

2. Traduisez les chaînes de caractères dans les fichiers `.po`.

3. Compilez les fichiers de traduction :

    ```sh
    django-admin compilemessages
    ```


Comment ajouter une nouvelle langue ?

Ajoutez la langue souhaitée à la liste LANGUAGES dans settings.py et créez les fichiers de traduction correspondants.
