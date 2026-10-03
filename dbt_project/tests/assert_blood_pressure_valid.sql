{{ config(severity='warn') }}

select record_id
from {{ ref('stg_tumores') }}
where diastolic_bp >= systolic_bp