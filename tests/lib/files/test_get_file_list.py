import os
import tempfile
import pytest
from pyrightfixer.lib.files import get_file_list


class TestGetFileList:
    def test_single_python_file(self):
        """Test that a single Python file is returned when given its path."""
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file.write(b'print("hello")')
            temp_file.flush()

            try:
                result = get_file_list(temp_file.name)
                assert len(result) == 1
                assert temp_file.name in result
            finally:
                os.unlink(temp_file.name)

    def test_non_python_file(self):
        """Test that non-Python files are not included."""
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
            temp_file.write(b"some text")
            temp_file.flush()

            try:
                result = get_file_list(temp_file.name)
                assert len(result) == 0
            finally:
                os.unlink(temp_file.name)

    def test_nonexistent_path(self):
        """Test that FileNotFoundError is raised for nonexistent paths."""
        with pytest.raises(
            FileNotFoundError, match="The path '/nonexistent/path' does not exist"
        ):
            get_file_list("/nonexistent/path")

    def test_directory_with_python_files(self):
        """Test that all Python files in a directory are found."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create some Python files
            py_file1 = os.path.join(temp_dir, "file1.py")
            py_file2 = os.path.join(temp_dir, "file2.py")
            txt_file = os.path.join(temp_dir, "file.txt")

            with open(py_file1, "w") as f:
                f.write('print("file1")')
            with open(py_file2, "w") as f:
                f.write('print("file2")')
            with open(txt_file, "w") as f:
                f.write("some text")

            result = get_file_list(temp_dir)

            # Should only include Python files
            assert len(result) == 2
            assert py_file1 in result
            assert py_file2 in result
            assert txt_file not in result

    def test_nested_directories(self):
        """Test that Python files in nested directories are found."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create nested directory structure
            sub_dir = os.path.join(temp_dir, "subdir")
            nested_dir = os.path.join(sub_dir, "nested")
            os.makedirs(nested_dir)

            # Create Python files at different levels
            root_py = os.path.join(temp_dir, "root.py")
            sub_py = os.path.join(sub_dir, "sub.py")
            nested_py = os.path.join(nested_dir, "nested.py")

            with open(root_py, "w") as f:
                f.write('print("root")')
            with open(sub_py, "w") as f:
                f.write('print("sub")')
            with open(nested_py, "w") as f:
                f.write('print("nested")')

            result = get_file_list(temp_dir)

            assert len(result) == 3
            assert root_py in result
            assert sub_py in result
            assert nested_py in result

    def test_empty_directory(self):
        """Test that an empty directory returns an empty list."""
        with tempfile.TemporaryDirectory() as temp_dir:
            result = get_file_list(temp_dir)
            assert result == []

    def test_directory_with_no_python_files(self):
        """Test that a directory with no Python files returns an empty list."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create some non-Python files
            txt_file = os.path.join(temp_dir, "file.txt")
            js_file = os.path.join(temp_dir, "file.js")

            with open(txt_file, "w") as f:
                f.write("some text")
            with open(js_file, "w") as f:
                f.write('console.log("hello")')

            result = get_file_list(temp_dir)
            assert result == []

    def test_relative_path_handling(self):
        """Test that relative paths are handled correctly."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a Python file
            py_file = os.path.join(temp_dir, "test.py")
            with open(py_file, "w") as f:
                f.write('print("test")')

            # Change to temp directory and use relative path
            original_cwd = os.getcwd()
            try:
                os.chdir(temp_dir)
                result = get_file_list(".")

                # Should find the Python file with absolute path
                assert len(result) == 1
                assert os.path.isabs(result[0])
                # Use realpath to resolve any symlinks (e.g., /var -> /private/var on macOS)
                assert os.path.realpath(result[0]) == os.path.realpath(py_file)
            finally:
                os.chdir(original_cwd)

    def test_file_with_py_in_name_but_no_extension(self):
        """Test that files with 'py' in name but no .py extension are not included."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create file with 'py' in name but wrong extension
            file_path = os.path.join(temp_dir, "python_file.txt")
            with open(file_path, "w") as f:
                f.write("some content")

            result = get_file_list(temp_dir)
            assert result == []

    def test_symbolic_links(self):
        """Test handling of symbolic links (if supported by the OS)."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a Python file
            py_file = os.path.join(temp_dir, "original.py")
            with open(py_file, "w") as f:
                f.write('print("original")')

            # Create a symbolic link (skip if not supported)
            link_file = os.path.join(temp_dir, "link.py")
            try:
                os.symlink(py_file, link_file)

                result = get_file_list(temp_dir)

                # Both original and link should be found
                assert len(result) >= 1  # At least the original file
                assert py_file in result
            except (OSError, NotImplementedError):
                # Symbolic links not supported on this system
                pytest.skip("Symbolic links not supported")
