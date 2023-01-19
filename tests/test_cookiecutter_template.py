import os
import shutil
import tempfile

import pytest


@pytest.fixture
def project_directory():
    # Create a temporary directory
    project_dir = tempfile.mkdtemp()

    # Run the cookiecutter command to generate the project files and directories in the temporary directory
    os.system(
        f"cookiecutter gh:NextGenMLOps/cookiecutter_ml_pipeline --no-input -o {project_dir}"
    )

    # Return the temporary directory
    yield os.path.join(project_dir, "name-of-the-project")

    # Clean up the temporary directory
    shutil.rmtree(project_dir)


def test_project_structure(project_directory):
    # Test that the required directories exist
    assert os.path.isdir(os.path.join(project_directory, "data"))

    assert os.path.isdir(os.path.join(project_directory, "data", "processed"))
    assert os.path.isdir(os.path.join(project_directory, "data", "raw"))
    assert os.path.isdir(os.path.join(project_directory, "docs"))
    assert os.path.isdir(os.path.join(project_directory, "src", "api"))
    assert os.path.isdir(os.path.join(project_directory, "src", "data"))
    assert os.path.isdir(os.path.join(project_directory, "src", "models"))
    assert os.path.isdir(os.path.join(project_directory, "tests"))


def test_required_files(project_directory):
    # Test that the required files exist
    assert os.path.isfile(os.path.join(project_directory, ".gitignore"))
    assert os.path.isfile(os.path.join(project_directory, "environment.yaml"))
    assert os.path.isfile(os.path.join(project_directory, "Dockerfile"))
    assert os.path.isfile(os.path.join(project_directory, "Makefile"))
    assert os.path.isfile(os.path.join(project_directory, "README.md"))
