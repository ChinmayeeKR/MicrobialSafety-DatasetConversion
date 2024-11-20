from static.paths import static_paths
from controller.LSVController import LSVController
from controller.JSONController import JsonController
import os
import json


def convert2squad(i_question: str, i_answer: str, i_context: str):
    """
    A mock function to demonstrate the convert2squad command.

    Args:
        question (str): Path to the question file.
        answer (str): Path to the answer file.
        context (str): Path to the context file.
    """
    print(f"Converting to SQuAD format using:\n"
          f"Question File: {i_question}\n"
          f"Answer File: {i_answer}\n"
          f"Context File: {i_context}")
    # Logic for conversion would go here.
    #  Make sure the context is a singular text entry
    raw_context = LSVController(i_context).to_list_of_str()
    context = process_context(raw_context)[0]

    list_of_q = LSVController(i_question).to_list_of_str()
    list_of_ans = LSVController(i_answer).to_list_of_str()

    # Create a JSON Controller
    jcObj = JsonController()
    jcObj.add_paragraph(context, list_of_q, list_of_ans)

    # Convert the jcObj instance to a JSON string
    json_string = json.dumps(jcObj.to_json(), indent=2)
    
    output_folder = static_paths["output_dir"]

    parent_dir = __get_parent_directory_name(i_path= i_context)

    file_path = os.path.join(output_folder, parent_dir+".json")

    # Write the JSON string to a text file
    try:
        with open(file_path, "w+") as file:
            file.write(json_string)
            print("Output for " + parent_dir + " written successfully.")

    except Exception as e:
        print("Error while writing the file:", str(e))

    print("Conversion complete.")


def process_context(lines: list[str]) -> tuple[str]:
    """
    Processes a list of strings from a context file and converts it into 
    a tuple containing a single concatenated string. Ignores multiple entries 
    or empty strings.

    Args:
        lines (list[str]): List of strings read from the context file.

    Returns:
        tuple[str]: A tuple containing a single concatenated string, 
                    or an empty tuple if input is invalid.
    """
    # Remove empty strings and strip whitespace
    valid_lines = [line.strip() for line in lines if line.strip()]

    # If more than one valid line exists, return an empty tuple
    if len(valid_lines) != 1:
        print(f"Warning: Context file should contain exactly one non-empty entry. Found {len(valid_lines)} entries.")
        return ()

    # Return a tuple containing the single valid line
    return (valid_lines[0],)


def __get_parent_directory_name(i_path: str) -> str:
    """
    Gets the parent directory name from a given path string and verifies its validity.

    Args:
        i_path (str): The input path string.

    Returns:
        str: The name of the parent directory if the path is valid. 
             Returns an empty string if the path is invalid or has no parent directory.
    """
    # Verify if the input path is a valid path
    if not os.path.exists(i_path):
        raise ValueError(f"The path '{i_path}' is not valid.")

    # Get the absolute path for safety
    abs_path = os.path.abspath(i_path)

    # Extract the parent directory
    parent_dir = os.path.dirname(abs_path)

    # Extract the name of the parent directory
    parent_name = os.path.basename(parent_dir)

    return parent_name
