import os

from solution.solution_start import Snowflake
from solution.solution_start import send_sqs_message

class TestStart(object):
    def test_connection_to_snowflake(self):
        snow = Snowflake()

        version = snow.exec_query("SELECT CURRENT_VERSION();")

        assert version.iloc[0]['CURRENT_VERSION()'] == '6.18.3', "Snowflake Version does not match the expected version."

    def test_sqs_send_receive(self):
            MESSAGES = [
                '{"addressee": "john.smith@sainsburys.co.uk", "message": "test1"}',
                '{"addressee": "jane.doe@sainsburys.co.uk", "message": "test2"}',
                '{"addressee": "jane.smith@sainsburys.co.uk", "message": "test3"}'
            ]

            for message in MESSAGES:
                send_sqs_message(message, 'test-sqs-messaging')                       
                        
            file = open('test-sqs-messaging.txt', mode='r')
            all_messages = file.readlines()
            file.close()

            line = 0
            for msg in all_messages:
                assert MESSAGES[line].strip() == msg.strip(), f"Message written: {msg} does not match expected message: {MESSAGES[line]}"
                line += 1
            print(f"\nThe messages written matches those expected.")

            assert line == 3, "Number of messages written, was not the number expected."
            print(f"\nThe number of messages written matches the expected number.")

            # Clean-up the test file.
            os.remove('test-sqs-messaging.txt')
