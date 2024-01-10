#
# Connect over TCP to the following server: 'localhost', 10000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

"""
----------------- WARNING -----------------
This script has roughly a 10% failure rate
due to the nature of the challenge. I
recommend running the script multiple times
before posting an issue on this repository...
"""

import socket
import sys

class Script:
  def __init__(self) -> None:
    """ Generates a lookup table of english words """
    self.english_lookup = set("".join(["WEDDING FEAST PREPARED ONCE FLAMES NOT UNTIL SAFELY OUT REPLIED ALADDIN ALL HIS HEART DAUGHTER INSTANT THE EARTH BENEATH THEIR FEET TREMBLED AND THEY HEARD HIM AND COMMANDED HIM ONCE SEARCH THE LAMP WHO THE POOR WOMAN WHO COMES HERE EVERY DAY ASKED BRING HER EXCLAIMED THIS THE VERY PLACE FOR WHICH HAVE BEEN EIGHTY SLAVES GARDEN SHINING FRUITS BUT COULD FIND WAY ESCAPE FOR TWO INSTANTLY THE STONE SLIPPED BACK INTO PLACE THE EARTH CLOSED OVER LOSE TIME OBEYING COMMANDS BEGAN LOOK ABOUT HIM WALLS FOR YOU YOU WILL CERTAINLY DIE WHEN YOU HAVE PASSED"]).split(" "))
    print("-"*50 + "\n" + "Generated lookup table:\n\n" + ", ".join([word for word in self.english_lookup]) + "\n" + "-"*50 + "\n")
  
  @staticmethod
  def make_connection(address: str, port: int) -> socket.socket:
    """ Connects to a server provided the address and port, then returns the client """
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((address, port))
    return client
  
  @staticmethod
  def ping(client: socket.socket, message: str) -> str:
    """ Sends a message to the connected server and returns the response """
    client.send(message.encode())
    return client.recv(1024).decode()
  
  @staticmethod
  def caesar_decrypt(text: str) -> str:
    """ Shifts a given text by one unicode value """
    result = ""

    for char in text:
        if char.isalpha():
            # Shift the character by 1 position to the right
            shifted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A') if char.isupper() else
                               (ord(char) - ord('a') + 1) % 26 + ord('a'))
            result += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result
  
  def is_english(self, text: str) -> bool:
    """ Checks if there are english words in the text (NOT 100% CONSISTENT) """
    for english_word in self.english_lookup:
      if english_word in text:
        print(f"\nWORD MATCHED: {english_word}")
        return True
    
    return False
  
  def slice(self, cipher: str) -> list:
    """ Slices the data retrieved from the server """
    return cipher.splitlines()[1:]
  
  def brute_force(self, cipher_text: str) -> str:
    """ Runs the caesar shift and english lookup, raises an error if it fails """
    print("-"*50)
    for shift in range(27):
      print(cipher_text)
      if self.is_english(cipher_text):
        print(f"\nDecrypted Text:\n{cipher_text}" + "\n" + "-"*50 + "\n")
        return cipher_text
      
      cipher_text = self.caesar_decrypt(cipher_text)
      
    raise RuntimeError("Decrypt Failed")
  
  def brute_force_multiple(self, ciphers: list) -> list:
    """ Runs the brute force on every sentence provided by the server,
    AND YES I KNOW ITS "INEFFICIENT", SHUT UP
    """
    return [self.brute_force(cipher) for cipher in ciphers]
  
  def package(self, messages: list) -> str:
    """ Reformats the decrypted text before sending it back to the server """
    return "\n".join(messages)
  
  def run(self) -> None:
    """ The highest level of abstraction for the script """
    client    = self.make_connection("localhost", 10000)
    response  = self.ping(client, "GET")
    ciphers   = self.slice(response)
    decrypted = self.brute_force_multiple(ciphers)
    packaged  = self.package(decrypted)
    flag      = self.ping(client, packaged)
    print(flag)
  
if __name__ == "__main__":
  script = Script()
  script.run()
