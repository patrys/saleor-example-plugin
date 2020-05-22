from setuptools import setup

setup(
    name="saleor-example-plugin",
    version="2.11.0",
    author="Mirumee Software",
    author_email="hello@mirumee.com",
    packages=["example_plugin"],
    entry_points={
        "saleor.plugins": [
            "example_plugin = example_plugin.plugin:ExamplePlugin"
        ]
    }
)
