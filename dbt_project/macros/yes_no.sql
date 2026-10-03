{% macro yes_no(column) %}
    case lower(trim({{ column }}))
        when 'yes' then true
        when 'no' then false
    end
{% endmacro %}