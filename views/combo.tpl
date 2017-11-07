<%
setdefault('value', -1)
setdefault('cols', str(12))
setdefault('disabled', False)

value_combo = value
bootstrap_cols = cols
is_disabled = disabled
%>
<select
    id="{{id_combo}}" 
    name="{{id_combo}}" 
    class="form-control col-md-{{bootstrap_cols}}"
    {{!'disabled="disabled"' if is_disabled else ''}}
>
    <option value="-1"></option>
    %for item in items:
    <option 
        value="{{item.get(value_name)}}"
        {{!'selected="selected"' if item.get(value_name) == value_combo else ''}}
    >
        {{item.get(text_name)}}
    </option>
    %end
</select>