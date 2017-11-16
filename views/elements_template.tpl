% rebase('page.tpl', title='Elementos')

<%
setdefault('cols', str(12))
bootstrap_cols = cols
%>

%if action == "view":
<div id="view" class="col-md-{{bootstrap_cols}} mt-5">
    <a href="/elements/create" class="col-md-auto btn btn-primary">Nuevo Elemento</a>
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Tipo</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for element in data_e.get("elements"):
            <tr data-element="{{element.get_id(True)}}"
                {{!'data-parent="element.get_parent_id()"' if element.get_parent_id() > 0 else ''}}
            >
                <td>
                    {{element.get_name()}}
                </td>
                <td>
                    % include('combo.tpl', value_name="id", text_name="name", items=data_e.get("element_types"), id_combo="typeId", value=element.get_type_id(), disabled=True, cols=12)
                </td>
                <td>
                    <a href="/elements/edit/{{element.get_id(True)}}" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/elements/delete/{{element.get_id(True)}}" data-btn="delete_element" class="btn btn-danger">Eliminar</a>
                </td>
                <!--
                %if element.is_active():
                <span class="badge badge-primary">
                    Activo
                </span>
                %else:
                <span class="badge badge-danger">
                    Inactivo
                </span>
                %end
                %if element.is_container():
                <span class="badge badge-light">
                    Contenedor
                </span>
                %end
                -->
            </tr>
            %end
        </tbody>
    </table>
</div>
%elif action == "edit" or action == "create":
%element = data_e.get("element")
<div class="col-md-{{bootstrap_cols}} mt-5">
    <form action="/elements/save/{{element.get_id(True)}}" method="POST" enctype="multipart/form-data">
        <div class="row">
            <div class="form-group col-md">
                <label for="name">Nombre</label>
                <input class="form-control" type="text" id="name" name="name" value="{{element.get_name()}}" />
            </div>
            <div class="content-form col-md">
                <label for="parent_id">Padre</label>
                % include('combo.tpl', value_name="id", text_name="name", items=data_e.get("elements"), id_combo="parent_id", value=element.get_parent_id())
            </div>
            <div class="content-form col-md">
                <label for="type_id">Tipo</label>
                % include('combo.tpl', value_name="id", text_name="name", items=data_e.get("element_types"), id_combo="type_id", value=element.get_type_id())
            </div>
        </div>
        <div class="form-check">
            <label class="form-check-label">
                <input class="form-check-input" type="checkbox"
                    id="is_container" name="is_container" value="it_is"
                    {{!'checked="checked"' if element.is_container() else ''}} />
                Contenedor
            </label>
        </div>
        <div class="form-group">
            <input class="col-md-auto btn btn-success" type="submit" value="Guardar" />
            <a class="col-md-auto btn btn-danger" href="javascript:void(0)" onclick="window.history.back();">Volver</a>
        </div>
    </form>
</div>
<div id="content" class="col-md-{{bootstrap_cols}} mt-5">

</div>
%end
