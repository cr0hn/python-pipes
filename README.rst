Python pipes
============

This projects allow to read stdin and detect if input data comes from a UNIX pipe and if the output is connected to a UNIX pipe.

Install
-------

.. code-block:: console

    > pip install python-pipes

How to use
----------

Basic example of a tool that read from info stdin:

.. code-block:: python

    # file: basic_example.py
    from python_pipes import read_stdin_lines

    def main():
        for is_stdin_pipe, is_stdout_pipe, line in read_stdin_lines():
            print("Input connected to pipe: ", is_stdin_pipe)
            print("Output  connected to pipe: ", is_stdout_pipe)
            print("Line read: ", line)


    if __name__ == '__main__':
        main()

Results depending of how to execute them:

.. code-block:: console

    $ python basic_example.py
    Input connected to pipe:  False
    Output  connected to pipe:  False
    Line read:  None
    $
    $ echo "hello" | python basic_example.py
    Input connected to pipe:  True
    Output  connected to pipe:  False
    Line read:  hello
    $
    $ echo "hello" | python basic_example.py | awk '{print $0}'
    Input connected to pipe:  True
    Output  connected to pipe:  True
    Line read:  hello