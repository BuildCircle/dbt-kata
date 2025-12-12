with source as (

    select * from {{ ref('raw_users') }}

),

renamed as (

    select distinct
        user_id,
        created_at

    from source

)

select * from renamed
