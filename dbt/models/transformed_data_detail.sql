with transformed_data as (
    select * from {{ ref('stg_transformed_data') }}
),

select *
from transformed_data
