#email = input("Your email address: ")

# "hello.worldcom"    => An email address has to contain a '@' character!
# "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
# "@world.com"        => The username before the '@' character cannot be empty!
# "hello@"            => The domain after the '@' character cannot be empty!
# "hello@worldcom"    => An email address has to contain at least one '.' character!
# "hell.o@worldcom"   => The domain has to contain at least one '.' character!
# "he.llo@worldcom."  => The top-level domain cannot be empty!
# "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
# ".hello@world.com"  => The username cannot start with a '.' character!
# "he.llo@.world.com" => The domain cannot start with a '.' character!
# "hello@world.com"   => Valid email address :)





error_message_no_at = "An email address has to contain a '@' character!" #kesz
error_message_too_many_at = "An email address cannot contain more than one '@' characters!" #kesz
error_message_no_dot = "An email address has to contain at least one '.' character!" #kesz
error_message_no_username = "The username before the '@' character cannot be empty!" #kesz
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!" #kesz
error_message_no_server_name = "The domain cannot start with a '.' character!" #kesz
error_message_no_tld = "The top-level domain cannot be empty!" #kesz
error_message_short_tld = "The top-level domain has to be at least two characters long!" #kesz
error_message_no_domain = "The domain after the '@' character cannot be empty!" #kesz
error_message_invalid_username = "The username cannot start with a '.' character!" #kesz
ok_message = "Valid email address :)"
is_valid = False

while not is_valid:
    email = input("Add meg az e-mail címed: ")
    length_of_email = len(email)
    number_of_at_characters = email.count("@")
    number_of_dot_characters = email.count(".")
    position_of_at = email.find("@")

    position_of_first_dot = email.find(".")
    position_of_last_dot = email.rfind(".")
    position_of_first_dot_after_the_at = email.find(".", position_of_at)

    if "@" not in email:
        print(error_message_no_at)
    elif email.count("@") > 1:
        print(error_message_too_many_at)
    elif email.endswith("@"):
        print(error_message_no_domain)
    elif "." not in email:
        print(error_message_no_dot)
    elif email.startswith("@"):
        print(error_message_no_username)

    elif position_of_first_dot_after_the_at < 1:
        print(error_message_no_dot_in_domain)
    elif position_of_first_dot_after_the_at == position_of_at + 1:
        print(error_message_no_server_name)
    elif email.endswith("."):
        print(error_message_no_tld)
    elif len(email.split(".")[-1]) < 2:
        print(error_message_short_tld)
    elif email.startswith("."):
        print(error_message_invalid_username)
    else:
        print(ok_message)
        is_valid = True
