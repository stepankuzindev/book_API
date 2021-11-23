# book_API

## Migrations

Create new migration
```console
$ alembic revision --autogenerate -m "Text"
```

Use new migrations
```console
$ alembic upgrade head
```

Downgrade last migration
```console
$ alembic downgrade -1
```
