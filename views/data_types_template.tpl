% rebase('page.tpl', title='Tipos de dato')

<%
setdefault('cols', str(12))
bootstrap_cols = cols
combo_tablas = [{"id":"NUMBER","name":"Número"}, {"id":"TEXT","name":"Texto"}]
%>

%if action == "view":
<div class="col-md-{{bootstrap_cols}} mt-5">
    <a href="/data_types/create" class="col-md-auto btn btn-primary">Nuevo Tipo</a>
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Tabla</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for data_type in data_e.get("data_types"):
            <tr data-type="{{data_type.get_id(True)}}">
                <td>
                    {{data_type.get_name()}}
                </td>
                <td>
                    % include('combo.tpl', value_name="id", text_name="name", items=combo_tablas, id_combo="table", value=data_type.get_table(), disabled=True, cols=12)
                </td>
                <td>
                    <a href="/data_types/edit/{{data_type.get_id(True)}}" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/data_types/delete/{{data_type.get_id(True)}}" data-btn="delete_element" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            %end
        </tbody>
    </table>
</div>
%elif action == "edit" or action == "create":
%data_type = data_e.get("data_type")
<div class="col-md-{{bootstrap_cols}} mt-5">
    <form action="/data_types/save/{{data_type.get_id(True)}}" method="POST" enctype="multipart/form-data">
        <div class="row">
            <div class="form-group col-md">
                <label for="name">Nombre</label>
                <input class="form-control" type="text" id="name" name="name" value="{{data_type.get_name()}}" />
            </div>
            <div class="content-form col-md">
                <label for="name">Tipo</label>
                % include('combo.tpl', value_name="id", text_name="name", items=combo_tablas, id_combo="table", value=data_type.get_table())
            </div>
        </div>
        <div class="form-group">
            <input class="col-md-auto btn btn-success" type="submit" value="Guardar" />
            <a class="col-md-auto btn btn-danger" href="javascript:void(0)" onclick="window.history.back();">Volver</a>
        </div>
    </form>
</div>
%end