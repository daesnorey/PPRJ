<%
setdefault('cols', str(12))
setdefault('embed', False)
bootstrap_cols = cols
%>

%if embed is True:
%reload = "/models/" + id_model + "/components/view #view"
%else:
%reload = "/components #view"    
%end

%if action == "view":
% rebase('parametrization.tpl', title='Componentes')
<div id="view" class="col-md-{{bootstrap_cols}} mt-5">
    %if embed is False:
        <a href="javascript:void(0)" data-link="/components/create" data-method="GET" data-btn="create_component" data-reload="{{reload}}" class="col-md-auto btn btn-primary">Nuevo Componente</a>
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
                    %if embed is False:
                    <a href="javascript:void(0)" data-link="/components/edit/{{component.get_id(True)}}" data-btn="edit_component" data-reload="{{reload}}" data-method="GET" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/components/delete/{{component.get_id(True)}}" data-btn="delete_component" data-reload="{{reload}}" class="btn btn-danger">Eliminar</a>
                    %else:
                    <a href="javascript:void(0)" data-link="/models/{{id_model}}/components/delete" data-id="{{component.get_id(True)}}"
                        data-btn="delete_component" data-reload="{{reload}}" class="btn btn-danger">X</a>
                    %end
                </td>
            </tr>
            %end
        </tbody>
    </table>
    %if embed is True:
    <a href="javascript:void(0)" data-link="/models/{{id_model}}/components/create" data-btn="create_model_component" data-method="GET" data-reload="/models/{{id_model}}/components/view #view" class="col-md-auto btn btn-primary">Agregar Componente</a>
    %end
</div>
%elif action == "edit" or action == "create":
%component = data_e.get("component")
<div class="col-md-{{bootstrap_cols}} mt-5 row">
    %if embed is True:
    %form_action = "/models/" + id_model + "/components/save"
    %else:
    %form_action = "/components/save/" + component.get_id(True)
    %end
    <div class="col-md-6 mt-5">        
        <form action="{{form_action}}" method="POST" enctype="multipart/form-data"
        data-form="component"
        data-reload="{{reload}}">
            <input type="hidden" id="id" name="id" value="{{component.get_id(True)}}" />
            <div class="form-group col-md-auto">
                <div class="row">
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
    %if embed is True:
    <div class="col-md-6">
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
                        <input type="checkbox" class="form-check-input" {{! 'checked="checked"' if componentG.is_generic() else ''}} disabled="disabled"
                        />
                    </td>
                    <td>
                        <a href="javascript:void(0)" data-link="/models/{{id_model}}/components/add" data-id="{{componentG.get_id(True)}}" data-btn="add_component"
                            data-reload="{{reload}}" class="btn">Agregar</a>
                    </td>
                </tr>
                %end
            </tbody>
        </table>
    </div>
    %else:
    <div class="col-md-12" data-load="/components/{{component.get_id(True)}}/elements/view #view">
    %end
    </div>
</div>
<div id="content" class="col-md-{{bootstrap_cols}} mt-5">

</div>
%end