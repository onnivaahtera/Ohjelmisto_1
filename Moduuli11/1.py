class Publication:
  def __init__(self, name: str) -> None:
    self.name = name

  def print_information(self) -> None:
    print(f"Name of publication: {self.name}")

class Book(Publication):
  def __init__(self, name: str, author: str, page_count: int) -> None:
    self.author = author
    self.page_count = page_count
    super().__init__(name)

  def print_information(self) -> None:
    super().print_information()
    print(f"Author: {self.author}, page count: {self.page_count}")

class Magazine(Publication):
  def __init__(self, name, cheif_editor):
    self.chief_editor = cheif_editor
    super().__init__(name)

  def print_information(self) -> None:
    super().print_information()
    print(f"Chief editor: {self.chief_editor}")


def main() -> None:
  Magazine("Donald Duck", "Aki Hyppä").print_information()
  print("\n")
  Book("Compartment No. 6", "Rosa Liksom", 192).print_information()


  
if __name__=="__main__":
  main()