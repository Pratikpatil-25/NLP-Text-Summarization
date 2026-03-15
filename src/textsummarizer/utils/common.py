import os
from box.exceptions import BoxValueError # It is used to handle errors related to ConfigBox or Box objects.
import yaml # YAML files are commonly used for configuration in ML projects.
from textsummarizer.logging import logger # This imports a custom logger from your project module called textSummarizer.
from ensure import ensure_annotations #It enforces attribute data type hints in functions.
from box import ConfigBox # python-box is a Python library that allows you to access dictionary values using dot notation instead of square brackets. ConfigBox is a special dictionary wrapper that converts a normal dictionary into an object so that keys can be accessed using dot notation.
from pathlib import Path #Used for working with file paths in a modern and clean way.
from typing import Any # Used in type hints when a variable can accept any data type.

@ensure_annotations  # python automatically manages data type handling, hence in some cases if we give wrong data type in the parameter of a function then it won't give error but an incorrect result and then we wouldn't know where we have made error in the code. Hence, if we use ensure_annotations decorator just before a function definition, it gives error in such cases and therefore lets us know that we have given a wrong parameter data type.
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """reads yaml file and returns  

    Args:
        path_to_yaml (str) : path like input
        e: empty file

    Raises:
        ValueError: If yaml file is empty

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file: 
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"