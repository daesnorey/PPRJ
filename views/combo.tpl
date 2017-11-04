<%
try:
    value_combo = value
except NameError:
    value_combo = -1
try:
    bootstrap_cols = cols
except NameError:
    bootstrap_cols = "12"
%>
<select value="{{value_combo}}" id="{{id_combo}}" name"{{id_combo}}" 
    class="form-control col-md-{{bootstrap_cols}}">
    <option value="-1">Select item</option>
    %for item in items:
    <option value="{{item.get(value_name)}}">
        {{item.get(text_name)}}
    </option>
    %end
</select>