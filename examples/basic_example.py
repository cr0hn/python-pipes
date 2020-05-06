from python_pipes import read_stdin_lines


def main():
    for is_stdin_pipe, is_stdout_pipe, line in read_stdin_lines():
        print("Input connected to pipe: ", is_stdin_pipe)
        print("Output  connected to pipe: ", is_stdout_pipe)
        print("Line read: ", line)


if __name__ == '__main__':
    main()

