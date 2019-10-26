from .ordered_load import ordered_load
import os.path as path
import logging
from glob import glob

from mako.template import Template

class Builder:

    def __init__(self, pwd:str):
        self._log = logging.getLogger("Builder")
        self._pwd = pwd

    def _read_file(self, filename):
        full_filename = path.join(self._pwd, filename)
        with open(full_filename) as f:
            return f.read()
            
    def _load_file(self, filename, _reader=None):
        if _reader is None:
            _reader = self._read_file

        raw_data = _reader(filename)
        return ordered_load(raw_data)

    def _get_template_name(self, filename):
        basename = path.basename(filename)
        head = basename.split(".")[0]

        return head


    def run(self):
        build_configuration = self._load_file("build.yml")

        for target_name, target in build_configuration.items():
            print(f"Processing target {target_name}")
            # load model's entities
            model_filenames = glob(path.join(self._pwd, target["model"]))
            models = [self._load_file(f) for f in model_filenames]
            
            # load template
            template_filenames = glob(path.join(self._pwd, target["template"]))
            templates = [(Template(filename=f), self._get_template_name(f)) for f in template_filenames]
            
            for m in models:
                for (t, t_name) in templates:
                    rendered = t.render(**m)
                    output_param = {
                        "pwd":self._pwd, 
                        "entity_name":m["name"], 
                        "template_name":t_name
                        }
                    output_path = target["output"].format(**output_param)

                    with open(output_path, "w") as f:
                        f.write(rendered)
