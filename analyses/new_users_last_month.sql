-- Analysis: new_users_last_month
-- Description: Counts new users created in the last month (simulated for this dataset)
select 
    count(*) as new_user_count 
from {{ ref('dim_users') }}
where created_at >= '2023-01-01'
