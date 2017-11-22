<%
setdefault('cols', str(12))
bootstrap_cols = cols
%>

%if action == "view":
% rebase('parametrization.tpl', title='Tipos de elementos')
<div id="view" class="col-md-{{bootstrap_cols}} mt-5">
    <a href="javascript:void(0)" data-link="/element_types/create" data-method="GET" data-btn="create_element_type" class="col-md-auto btn btn-primary">Nuevo Tipo</a>
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Tag</th>
                <th>Tipo</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for element_type in data_e.get("element_types"):
            <tr data-element="{{element_type.get_id(True)}}">
                <td>
                    {{element_type.get_name()}}
                </td>
                <td>
                    {{element_type.get_tag()}}
                </td>
                <td>
                    % include('combo.tpl', value_name="id", text_name="name", items=data_e.get("data_types"), id_combo="data_type_id", value=element_type.get_data_type_id(), disabled=True, cols=12)
                </td>
                <td>
                    <a href="javascript:void(0)" data-link="/element_types/edit/{{element_type.get_id(True)}}" data-btn="edit_element" data-method="GET" data-reload="/element_types #view" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/element_types/delete/{{element_type.get_id(True)}}" data-btn="delete_element" data-reload="/element_types #view" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            %end
        </tbody>
    </table>
</div>
%elif action == "edit" or action == "create":
%element_type = data_e.get("element_type")
<div class="col-md-{{bootstrap_cols}} mt-5">
    <form 
        action="/element_types/save/{{element_type.get_id(True)}}" method="POST" enctype="multipart/form-data"
        data-form="element_type_form"
        data-reload="/element_types #view">
        <div class="row">
            <div class="form-group col-md">
                <label for="name">Nombre</label>
                <input class="form-control" type="text" id="name" name="name" value="{{element_type.get_name()}}" />
            </div>
            <div class="content-form col-md">
                <label for="name">Tag</label>
                <input class="form-control" type="text" id="tag" name="tag" value="{{element_type.get_tag()}}" />
            </div>
            <div class="content-form col-md">
                <label for="name">Tipo</label>
                % include('combo.tpl', value_name="id", text_name="name", items=data_e.get("data_types"), id_combo="data_type_id", value=element_type.get_data_type_id())
            </div>
        </div>
        <div class="form-check">
            <label class="form-check-label">
                <input class="form-check-input" type="checkbox" 
                    id="is_parent" name="is_parent" value="it_is"
                    {{!'checked="checked"' if element_type.is_parent() else ''}} />
                Padre
            </label>
        </div>
        <div class="form-group">
            <input class="col-md-auto btn btn-success" type="submit" value="Guardar" />
            <a class="col-md-auto btn btn-danger" href="javascript:void(0)" onclick="window.history.back();">Volver</a>
        </div>
    </form>
</div>
%end