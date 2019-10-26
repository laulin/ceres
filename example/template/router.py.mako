from flaskon import router
%for k, v in models.items():
from request_${k} import ${v["variables"]["action"]}_${k}
%endfor

%for k, v in models.items():
router("${v["variables"]["path"]}", ${v["variables"]["action"]}_${k})
%endfor

app.run()