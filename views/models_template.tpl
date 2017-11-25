
<%
setdefault('cols', str(12))
bootstrap_cols = cols
%>

%if action == "view":
% rebase('parametrization.tpl', title='Modelos')
<div id="view" class="col-md-{{bootstrap_cols}} mt-5">
    <a href="javascript:void(0)" data-link="/models/create" data-method="GET" data-btn="create_model" data-reload="/models #view" class="col-md-auto btn btn-primary">Nuevo Modelo</a>
    <table class="table">
        <thead>
            <tr>
                <th>Nombre</th>
                <th>Accion</th>
            </tr>
        </thead>
        <tbody>
            %for model in data_e.get("models"):
            <tr>
                <td>
                    {{model.get_name()}}
                </td>
                <td>
                    <a href="javascript:void(0)" data-link="/models/edit/{{model.get_id(True)}}" data-btn="edit_model" data-reload="/models #view" data-method="GET" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/models/delete/{{model.get_id(True)}}" data-btn="delete_model" data-reload="/models #view" class="btn btn-danger">Eliminar</a>
                </td>
            </tr>
            %end
        </tbody>
    </table>
</div>
%elif action == "edit" or action == "create":
%model = data_e.get("model")
<div class="col-md-12 mt-5"></div>
<div class="col-md-4 mt-5">
    <form 
        action="/models/save/{{model.get_id(True)}}" method="POST" enctype="multipart/form-data"
        data-form="model"
        data-reload="/models #view">
        <div class="row">
            <div class="form-group col-md">
                <label for="name">Nombre</label>
                <input class="form-control" type="text" id="name" name="name" value="{{model.get_name()}}" />
            </div>
        </div>
        <div class="form-group">
            <input class="col-md-auto btn btn-success" type="submit" value="Guardar" />
            <a class="col-md-auto btn btn-danger" href="javascript:void(0)" onclick="window.history.back();">Volver</a>
        </div>
    </form>
</div>
<div class="col-md-12" data-load="/models/{{model.get_id(True)}}/components/view #view">
</div>
%end
