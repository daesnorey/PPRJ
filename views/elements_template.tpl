% rebase('page.tpl', title='Elementos')

%if action == "view":
<div class="row col-md-10 col-md-offset-1">
    <ul class="row col-md-12">
        %for element in data_e.get("elements"):
        <li class="row col-md-10" 
            data-element="{{element.get_id(True)}}" 
            {{!'data-parent="element.get_parent_id()"' if element.get_parent_id() > 0 else ''}}
        >
            <span class="row col-md-4">
                {{element.get_name()}}
            </span>
            <span>
                {{element.get_type_id()}}
            </span>
        </li>
        %end
    </ul>
</div>
%end

% include('combo.tpl', value_name="id", text_name="name", items=data_e.get("elements"), id_combo="tmp")
% include('combo.tpl', value_name="id", text_name="name", items=data_e.get("element_types"), id_combo="tmp")
% include('combo.tpl', value_name="id", text_name="name", items=data_e.get("data_types"), id_combo="tmp")