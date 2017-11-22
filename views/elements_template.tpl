
<%
setdefault('cols', str(12))
setdefault('embed', False)
bootstrap_cols = cols
%>

%if action == "view":
% rebase('parametrization.tpl', title='Elementos')
<div id="view" class="col-md-{{bootstrap_cols}} mt-5">
    %if embed is False:
    <a href="javascript:void(0)" data-link="/elements/create#e_action" data-method="GET" class="col-md-auto btn btn-primary" data-btn="create_element">Nuevo Elemento</a>
    %end
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
                    %if embed is False:
                    <a href="javascript:void(0)" data-link="/elements/edit/{{element.get_id(True)}}" data-btn="edit_element" data-method="GET" data-reload="/elements #view" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/elements/delete/{{element.get_id(True)}}" data-btn="delete_element" data-reload="/elements #view" class="btn btn-danger">Eliminar</a>
                    %else:
                    <a href="javascript:void(0)" data-link="/components/{{id_component}}/elements/delete" data-id="{{element.get_id(True)}}" data-btn="delete_element" data-reload="/components/{{id_component}}/elements/view #view" class="btn btn-danger">X</a>
                    %end
                </td>
            </tr>
            %end
        </tbody>
    </table>
    %if embed is True:
    <a href="javascript:void(0)" data-link="/components/{{id_component}}/elements/create" data-btn="create_element" data-method="GET" data-reload="/components/{{id_component}}/elements/view" class="col-md-auto btn btn-primary">Agregar Elemento</a>
    %end
</div>
%elif action == "edit" or action == "create":
%element = data_e.get("element")
<div id="e_action" class="col-md-{{bootstrap_cols}} mt-5">
    %if embed is True:
    %form_action = "/components/" + id_component + "/elements/save"
    %reload = "/components/" + id_component + "/elements/view #view"
    %else:
    %form_action = "/elements/save/" + element.get_id(True)
    %reload = "/elements #view"    
    %end
    <form 
        action="{{form_action}}" method="POST" enctype="multipart/form-data"
        data-form="element_form"
        data-reload="{{reload}}">
        <input type="hidden" id="id" name="id" value="{{element.get_id(True)}}" />
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
            %if embed is True:
            <div class="content-form col-md">
                <label for="type_id">Posición</label>
                % include('combo.tpl', value_name="id", text_name="name", items=[{'id':1, 'name':'Izquierda'}, {'id':2, 'name':'Derecha'}, {'id':3, 'name':'Completa'}], id_combo="position")
            </div>
            %end
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
