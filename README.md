
Database backup:
docker compose exec -T wagtail_db pg_dump -U wagtail wagtail_db | gzip > ./backup_db_$(date +%Y%m%d_%H%M%S).sql.gz


# Decompress and pipe the backup file into the running PostgreSQL container
gunzip < [BACKUP_FILE_NAME].sql.gz | docker compose exec -i wagtail_db psql -U [DB_USER] -d [DB_NAME]