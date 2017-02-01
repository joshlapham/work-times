## How to Make it Go

- update `MYSQL_DATABASE` variable in `work_times_mysql_cfg.py`
- import database schema: `mysql -u root -h localhost {{ YOUR DATABASE NAME }} < work_times.sql`
- backup database: `mysqldump -u root -p {{ YOUR DATABASE NAME }} > work_times_backup.sql`
- un-comment calls to `record_time` method in `work_times.py` to save to database
- update date values in `work_times.py`
- see total hours for the week: `python work_times.py`
