-- Singular test: Fails if any user_id is not positive
select
    user_id
from {{ ref('dim_users') }}
where user_id <= 0
