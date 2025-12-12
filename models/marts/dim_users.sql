with stg_users as (

    select * from {{ ref('stg_users') }}

)

select * from stg_users
