% rebase('page.tpl', title='Modelos')

<%
setdefault('cols', str(12))
bootstrap_cols = cols
%>

%if action == "view":
<div class="col-md-{{bootstrap_cols}} mt-5">

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
                    <a href="/models/edit/{{model.get_id(True)}}" class="btn btn-primary">Editar</a>
                    <a href="javascript:void(0)" data-link="/models/delete/{{model.get_id(True)}}" data-button="" class="btn btn-danger" >Eliminar</a>
                </td>
                <!--
                %if model.is_active():
                <span class="badge badge-primary">
                    Activo
                </span>
                %else:
                <span class="badge badge-danger">
                    Inactivo
                </span>
                %end

                -->
            </tr>
            %end
        </tbody>
    </table>
</div>
%elif action == "edit" or action == "create":
%model = data_e.get("model")
<div class="col-md-{{bootstrap_cols}} mt-5">
    <form action="/models/save/{{model.get_id(True)}}" method="POST" enctype="multipart/form-data">
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
%end
