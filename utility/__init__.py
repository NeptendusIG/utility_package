"""utility package"""

from utility.function_dir import GUI, Settings, File
from utility.function_dir import InputUtil, OutNetwork

print("initialized")
__version__ = "1.3.0"


__help__ = """
# -- UTILITY PACKAGE --

- Settings
    setup_logging_json(cls, path_logconfig="logconfig.json"):
    setup_logging(cls, logger_name="main"):
    setlog_module(cls, config_module, logger_name="main"):
    relaunch_program(cls):
    relaunch_package(cls, package_name):
    launch_package(cls, package_name):

- InputUtil
    ...

- File
    copy_file_to(cls, base_file_path, directory_location):
    open_file(cls, file_path):
    create_file(cls, path, can_make_dirs=True, default_content=None, indent=4):
    add_line(cls, filepath, information, line_index=-1):
    delete_line(cls, filepath, line_index):
    - class JsonFile:
        check_and_load_jsondict(cls, jsonfile_path: str, handle_FileNotFound=False, handle_FileTypeError=False, handle_JsonError=False, handle_DataTypeError=False) -> dict | None:
        get_value_jsondict(cls, jsonfile_path: str, key: str, default=None, handle_keyERROR=False, **kwargs):
        set_value_jsondict(cls, jsonfile_path, key, value, can_modify_key=True, can_add_key=True):
    - class JsonLine:
        made_list_of_jsonline(cls, filename):
        add_a_jsonline(cls, information, filename="data/paths_list.json", tuple_rather_list=True):

- Formatting

- OutNetwork

- GetData

- GUI
    set_basic_window(cls, title="Tableau des commandes", level="auto", themename="journal", size=""):
    ask_yes_no(cls, titre, question):
    ask_file(cls, context="fichier", types=[("Fichier", "*.*")], multiple=False):
    ask_dir(cls, root=None, initialdir=os.getcwd(), can_cancel=True):
    set_cmd_buttons(cls, window, commandes):
    ask_entry(cls, title="Entrez le mot de passe", size="250x100", can_cancel=True) -> str:
    window_with_entry_labeled(cls, fields_entries, title="Enregistrer un compte", window=None):
    parse_buttons_on_object(cls, objet_to_str_list: iter, buttons_func_dict: dict[str: callable], window,


"""