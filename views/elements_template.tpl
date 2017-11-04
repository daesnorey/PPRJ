% include('head.tpl', title='Elementos')

%if action == "view":
<h2>{{action}}</h2>
%else:
<h2>otro</h2>
%end

<ul>
    %for element in elements:
    <li>{{element.get_name()}}</li>
    %end
</ul>

% include('foot.tpl')