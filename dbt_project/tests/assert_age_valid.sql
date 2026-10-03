select record_id
from {{ ref('stg_tumores') }}
where age < 0 or age > 120