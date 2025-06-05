import os
from setuptools import setup
from setuptools_scm import get_version

def version_with_branch(version):
    # If we're on main / a tag → just use the tag (e.g. “1.2.3”).
    branch = os.getenv("GITHUB_REF_NAME", "main")
    tag = version.tag or ""
    if branch == "main" and tag:
        return tag
    # Otherwise, append “+<branch>.<distance>.g<sha>”
    return version.format_with("{tag}+{branch}.{distance}.g{sha}")

setup(
    use_scm_version={
        "version_scheme": version_with_branch,
        "local_scheme": version_with_branch,
    },
    # All other fields are read from pyproject.toml
)
