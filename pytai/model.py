import sys
import importlib
import inspect

from pathlib import Path
from typing import Union, Any, Tuple

#from .common import *

class Parser(object):
    def __init__(self) -> None:
        pass

    def parse(self, path_file: Union[str, Path]) -> Any:
        """Parse the given file.
        
        Args:
            path_file:
                The path to the file to be parsed.
        
        Returns:
            A parser-specific object that can be used to iterate the internal structure of the
            file using get_children().
        """
        raise NotImplementedError("Inheriting classes must implement this method")

    def get_children(self, parent: Any) -> Tuple[str, Any]:
        """An iterator over the name and value of the children of the given parent.
        
        Args:
            parent: 
                An object as returned by parse() or get_children()

        Returns:
            A generator serving tuples containing the name of the child (str) and 
            the value of the child (arbitrary object).
            The value can either be a parser-specific object representing a structure
            or an integral type such as a list, string, integer, enum etc.
        """
        raise NotImplementedError("Inheriting classes must implement this method")

    

class KaitaiParser(Parser):

    def __init__(self, path_ksy: Union[str, Path], disable_cache: bool = False) -> None:
        """Create a Kaitai Parser.
        
        Args:
            disable_cache:
                If True, will always try to generate the parser from scratch using KSC
        """
        super().__init__()

        self.disable_cache = disable_cache

        # Create autogen folder and add it to path
        script_dir = Path(__file__).resolve().parent
        autogen_dir = script_dir / "tmp" / "autogen"
        autogen_dir.mkdir(parents = True, exist_ok = True)
        sys.path.append(str(autogen_dir.resolve()))

        importlib.import_module('kaitaistruct')

        self._load_parser(path_ksy)

    def _load_parser(self, path_ksy: Union[str, Path]) -> None:
        """Load and return a Kaitai parser matching the given Kaitai Struct language definition (*.ksy).

        Will first try to load a previously-generated parser (unless disable_cache was defined during init).
        Otherwise will try to compile the parser using KSC and the given *.ksy file.
        
        Args:
            path_ksy: 
                Path to Kaitai Struct language (*.ksy) file.
        """
        try:
            if self.disable_cache:
                raise RuntimeError("Cache disabled")

            parser_module = importlib.import_module(Path(path_ksy).stem)
            module_classes = [m[0] for m in inspect.getmembers(parser_module, inspect.isclass) if m[1].__module__ == parser_module.__name__]
            if len(module_classes) != 1:
                raise RuntimeError("Can't determine class name using introspection")
            main_class_name: str = module_classes[0]
        except (ImportError, RuntimeError):
            raise # TODO: Use KSC

        self.parser = getattr(parser_module, main_class_name)

    def parse(self, path_file: Union[str, Path]) -> "KaitaiStruct":
        try:
            parsed_file = self.parser.from_file(path_file)
            parsed_file._read()
        except Exception:
            raise

        return parsed_file

    def get_children(self, parent: "KaitaiStruct") -> Tuple[str, Any]:
        if hasattr(parent, "SEQ_FIELDS"):
            for child in parent.SEQ_FIELDS:
                yield (child, getattr(parent, child) )


class Model(object):

    def __init__(self):
        self.parsers = {}

    def get_parser(self, **kwargs) -> Parser:
        """Return a parser to parse the required files.

        Keyword Args:
            path_ksy:
                Path to Kaitai Structure definition (*.ksy file).
                Given this parameter, the returned parser will be 
                a KaitaiParser instance.

        Returns:
            The appropriate parser based on the keyword args.       
        """
        if "path_ksy" in kwargs:
            try:
                parser = self.parsers[kwargs["path_ksy"]]
            except KeyError:
                parser = KaitaiParser(kwargs["path_ksy"])
                self.parsers[kwargs["path_ksy"]] = parser
            
            return parser
        
        raise RuntimeError("Can't identify appropriate parser type")

        


        