package(default_visibility = ["//visibility:public"])
load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "validate_proxy",
    srcs = ["validate_proxy.py"],
    deps = [
        "//src/utils/git:repo",
    ],
    python_version = "PY3",
)
