# Release Process

   1. Run tests:
      ```
      python3 ./tests/test_application.py
      ```

   1. Run manual tests:
      ```
      python3 ./__main__.py
      ```

   1. Remove "`dist`" directory if it exists
      ```
      rm -rf dist
      ```

   1. Ensure that all changes are committed and pushed to GitHub:
      ```
      git status
      ```

   1. Create new tag: 
      ```
      git tag
      git tag vX.Y.Z
      ```

   1. Pack release:
      ```
      python3 packer.py
      ```

   1. Create Python Virtual Environment:
      ```
      python3 -m venv pytai-env
      source pytai-env/bin/activate
      ```

   1. Install `pypi`-related packages:
      ```
      pip install --upgrade build
      pip install --upgrade twine
      ```

   1. Build: 
      ```
      python3 -m build
      ```

   1. Upload to `testpypi`:
      ```
      python3 -m twine upload --repository testpypi dist/* --verbose
      ```

   1. Install new release from `testpypi`:
      ```
      pip install --index-url https://test.pypi.org/simple/ --no-deps pytai-hex
      ```

   1. Test release:
      ```
      pytai
      ```

   1. Uninstall release:
      ```
      pip uninstall pytai-hex
      ```

   1. Upload to `pypi`:
      ```
      python3 -m twine upload --repository pypi dist/* --verbose
      ```

   1. Install new release from `pypi`:
      ```
      pip install pytai-hex
      ```

   1. Test release:
      ```
      pytai
      ```

   1. Deactivate virtual environment:
      ```
      deactivate
      ```

   1. Remove virtual environment:
      ```
      rm -rf pytai-env
      ```

   1. Cleanup build:
      ```
      rm -rf dist
      rm -rf pytai_hex.egg-info
      ```

   1. Push tag:
      ```
      git push origin --tags
      ```

   1. Upload `pytai.pyz` to GitHub
