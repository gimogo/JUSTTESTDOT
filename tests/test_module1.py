# tests/test_module1.py

from my_project.module1 import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
