message = "Hello World!"

with open("0023_files_file.txt") as file:
    file.write(message)

# Test
written_message = ""
with open("0023_files_file.txt") as file:
    written_message = file.read()


# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert written_message == message, "Expected message to be written to file"
print("ok")
