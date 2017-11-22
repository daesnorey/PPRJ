% rebase('page.tpl', title='Componentes')

<%
setdefault('cols', str(12))
setdefault('embed', False)
bootstrap_cols = cols
%>

%if action == "view":
<div class="col-md-{{bootstrap_cols}} mt-5">
    %if embed is False:
        <a href="/components/create" class="col-md-auto btn btn-primary">Nuevo Componente</a>
    %end
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Generico</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for component in data_e.get("components"):
            <tr>
                <td>
                    {{component.get_name()}}
                </td>
                <td>
                    <input type="checkbox" class="form-check-input" {{!'checked="checked"' if component.is_generic() else ''}} disabled="disabled" />
                </td>
                <td>
                    <a href="/components/edit/{{component.get_id(True)}}" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/components/delete/{{component.get_id(True)}}" data-btn="delete_component" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            %end
        </tbody>
    </table>
    %if embed is True:
    <a href="/models/{{id_model}}/components/create" class="col-md-auto btn btn-primary">Agregar Componente</a>
    %end
</div>
%elif action == "edit" or action == "create":
%component = data_e.get("component")
<div class="col-md-{{bootstrap_cols}} mt-5">
    %if embed is True:
    %form_action = "/models/" + id_model + "/components/save"
    %else:
    %form_action = "/components/save/" + component.get_id(True)
    %end
    <form action="{{form_action}}" method="POST" enctype="multipart/form-data">
        <input type="hidden" id="id" name="id" value="{{component.get_id(True)}}" />
        %if embed is True:
        <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Generico</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for componentG in data_e.get("components"):
            <tr>
                <td>
                    {{componentG.get_name()}}
                </td>
                <td>
                    <input type="checkbox" class="form-check-input" {{!'checked="checked"' if componentG.is_generic() else ''}} disabled="disabled" />
                </td>
                <td>
                    <a href="javascript:void(0)" data-link="/models/{{id_model}}/components/add" data-id="{{componentG.get_id(True)}}" data-btn="add_component" class="btn">Agregar</a>
                </td>
            </tr>
            %end
        </tbody>
        </table>
        %end
        <div class="row">
            <div class="form-group col-md">
                <label for="name">Nombre</label>
                <input class="form-control" type="text" id="name" name="name" value="{{component.get_name()}}" />
            </div>
        </div>
        <div class="form-check">
            <label class="form-check-label">
                <input class="form-check-input" type="checkbox"
                    id="is_generic" name="is_generic" value="it_is"
                    {{!'checked="checked"' if component.is_generic() else ''}} />
                Generico
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