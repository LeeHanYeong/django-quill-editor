# Migrating to QuillField

To convert a field used as a **TextField** or **CharField** to a **QuillField**, the following operations are required.

Suppose you had a model that looked like this.

```python
# Assuming this is the model you created in the posts app
class NonQuillPost(models.Model):
    content = models.TextField()
```

1. Convert existing data into a format suitable for QuillField using django command.  

   **❗️USE WITH CAUTION❗️**  
   This command permanently transforms the contents of that field in the DB.

   ```shell
   # Usage: python manage.py convert_to_quill {app_name} {model_name} {field_name}
   > python manage.py convert_to_quill posts NonQuillPost content
   ```

2. Change existing field to QuillField.  

   ```python
   from django_quill.fields import QuillField
   
   class NonQuillPost(models.Model):
       content = QuillField()
   ```

3. Create a migration.  

   ```shell
   > python manage.py makemigrations
   Migrations for 'posts':
     posts/migrations/0002_alter_nonquillpost_content.py
       - Alter field content on nonquillpost
   ```

4. Apply the migration.  

   ```shell
   > python manage.py migrate
   Operations to perform:
     Apply all migrations: admin, auth, contenttypes, posts, sessions
   Running migrations:
     Applying posts.0002_alter_nonquillpost_content... OK
   ```
