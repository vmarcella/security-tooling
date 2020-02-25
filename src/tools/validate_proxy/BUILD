load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "validate_proxy",
    srcs = ["validate_proxy.py"],
    deps = [
        "//src/py_utils/git:get_repo",
    ]
    python_version = "PY3",
)
