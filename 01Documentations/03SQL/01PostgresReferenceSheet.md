## 1. Check if PostgreSQL is online
```bash
pg_lsclusters
```
If the cluster is down, you may see something like:
```text
16  main    5432 down
```

## 2. Start a PostgreSQL cluster
```bash
sudo pg_ctlcluster 16 main start
```

## 3. Connect to PostgreSQL with psql

### Method 1: Use the local postgres operating-system account
```bash
sudo -u postgres psql
```
If successful, the prompt will look like:
```text
postgres=#
```
Connect to a database:
```psql
\c ecom
```
The prompt then becomes something like `ecom=#`.

### Method 2: Connect with a PostgreSQL role and password
```bash
psql -U postgres -h localhost -d ecom -W
```

- `-U postgres`: PostgreSQL role to use.
- `-h localhost`: connect to the PostgreSQL server on this machine.
- `-d ecom`: database to connect to.
- `-W`: prompt for a password.

## 4. Exit psql
```psql
\q
```

## 5. Database navigation and inspection

### List databases
```psql
\l
```

### Connect to a database
```psql
\c database_name
```
Example:
```psql
\c ecom
```

### List tables in the current database
```psql
\dt
```

### Describe a table (columns, types, constraints)
```psql
\d table_name
```
Example:
```psql
\d products
```

### List roles/users
```psql
\du
```

## 6. Inspect table columns with SQL

Use this when you want a query result rather than the psql table-description view:
```sql
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name = 'products'
ORDER BY ordinal_position;
```
Replace `products` with the table name.

## 7. Database management

### Create a database
Run while connected to a different database:
```sql
CREATE DATABASE ecom;
```

### Drop a database
You cannot drop the database to which your current session is connected. Connect elsewhere first, for example:
```psql
\c postgres
```
Then:
```sql
DROP DATABASE ecom;
```

If connections are preventing the drop, PostgreSQL versions that support `WITH (FORCE)` can attempt to terminate them:
```sql
DROP DATABASE ecom WITH (FORCE);
```
This permanently deletes the database and its data. `WITH (FORCE)` may still fail if sessions cannot be terminated or other conditions prevent the drop.

### List databases owned by a role
```sql
SELECT datname
FROM pg_database
WHERE datdba = (SELECT oid FROM pg_roles WHERE rolname = 'your_username')
  AND datistemplate = false;
```
Replace `your_username` with the PostgreSQL role name. This lists databases owned by that role; it does not imply that the role created them.

### Generate and execute DROP commands for databases owned by a role
Run from `psql` while connected to a different database. Review the filter carefully before executing:
```psql
SELECT format('DROP DATABASE %I WITH (FORCE);', datname)
FROM pg_database
WHERE datdba = (SELECT oid FROM pg_roles WHERE rolname = 'your_username')
  AND datistemplate = false
  AND datname <> current_database()
\\gexec
```
`\\gexec` is a psql meta-command that executes each SQL statement returned by the query. Exclude any databases you want to keep (for example, add `AND datname NOT IN ('postgres', 'ecom')` as appropriate). PostgreSQL template databases should be retained; `template0` is excluded by `datistemplate = false`.

### Recreate a database
```sql
CREATE DATABASE ecom;
```

### Important notes about default databases
A standard PostgreSQL cluster normally includes:
- `postgres`: a convenient database for administration.
- `template0`: a pristine template database.
- `template1`: the default template used when creating databases.
Keep these default databases. Your application's database (such as `ecom`) is separate.

## 8. Quick reference

| Task | Command |
|---|---|
| Check PostgreSQL clusters | `pg_lsclusters` |
| Start cluster 16/main | `sudo pg_ctlcluster 16 main start` |
| Connect as OS postgres user | `sudo -u postgres psql` |
| Connect with password prompt | `psql -U postgres -h localhost -d ecom -W` |
| List databases | `\\l` |
| Connect to a database | `\\c database_name` |
| List tables | `\\dt` |
| Describe a table | `\\d table_name` |
| List roles | `\\du` |
| Exit psql | `\\q` |
| Drop a database | `DROP DATABASE database_name;` |
