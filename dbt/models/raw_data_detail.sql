with raw_data as (
    select * from {{ ref('stg_raw_data') }}
),

select *
from raw_data
