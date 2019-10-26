def ${variables["action"]}_${name}(\
%for k, v in entity.items():
${k}:${v["type"]}${'):' if loop.last else ', '}\
%endfor

    tmp = \
%for k, v in entity.items():
str(${k})${'' if loop.last else ' + '}\
%endfor

    if len(tmp) < 5:
        return ${variables["on_fail"]}
    else:
        return ${variables["on_success"]}