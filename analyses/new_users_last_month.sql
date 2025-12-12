-- Analysis: Users who signed up in the last month
select *
from {{ ref('dim_users') }}
where created_at >= date('now', '-1 month') -- Syntax may vary by warehouse (this is SQLite/DuckDB friendly)
-- For Snowflake/Postgres: where created_at >= current_date - interval '1 month'
