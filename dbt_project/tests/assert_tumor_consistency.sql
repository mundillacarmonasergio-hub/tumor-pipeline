{{ config(severity='warn') }}

select record_id
from {{ ref('stg_tumores') }}
where tumor_type = 'malignant' and brain_tumor_present = false