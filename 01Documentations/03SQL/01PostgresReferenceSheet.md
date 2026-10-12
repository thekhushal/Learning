## 1. Check if psql is online
```psql
pg_lsclusters
```
if it's down you'll see something like
```error
16  main    5432 down
```

## 2. To activate psql
```psql
sudo pg_ctlcluster 16 main start
```

## 3. Connect to psql

#### Method 1. No password needed: linux authorizes itself
```psql
sudo -u postgres psql
```
if successful you'll get something like 
```text
postgres=#
```
and
```psql
\c ecom
```
once connected you should see 
```text
ecom=#
```
- "postgres=#" means you are connected to psql, you can now connect to any database using" \c database"

#### Method 2. You'll be prompted to enter password
```psql
psql -U postgres -h localhost -d ecom -W
```
Breakdown
```text
-U postgres   → PostgreSQL user
-h localhost  → PostgreSQL server on your machine
-d ecom       → connect to the ecom database
-W            → prompt for password
```
once connected you should see
```text
ecom=#
```

## 4. To exit / quit
```psql
\q
```

## 5. Basic commands for navigation in
```text
postgres=#
```

#### 1. Lists all the databases under this user
```psql
\l
```

#### 2. To connect to a Database
```text
\c Database_Name
```
example,
```psql
\c ecom
```

