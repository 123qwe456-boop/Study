import os

# Define file names
file1 = "math_notes.txt"
file2 = "science_notes.txt"
merged_file = "merged_study_notes.txt"


def create_sample_files():
  """Creates two subject notes files if they do not already exist."""
  with open(file1, "w", encoding="utf-8") as f1:
    f1.write(
        "Mathematics study notes.\nTopics include algebra, geometry, and"
        " calculus.\n"
    )

  with open(file2, "w", encoding="utf-8") as f2:
    f2.write(
        "Science study notes.\nTopics include biology, chemistry, and"
        " physics.\n"
    )


def count_words(filename):
  """Reads a file safely using with open() and counts words using split()."""
  total_words = 0
  with open(filename, "r", encoding="utf-8") as file:
    for line in file:
      words = line.split()  # Splits the line into a list of words
      total_words += len(words)
  return total_words


def organize_study_notes():
  # 1. Create the two subject notes files
  create_sample_files()

  # 2. Check whether a merged file already exists
  if os.path.exists(merged_file):
    print(f"'{merged_file}' already exists.")
    # 5. Remove old file when required
    os.remove(merged_file)
    print(f"Removed old '{merged_file}'.")

  # 3. Read files safely and count words
  c1 = count_words(file1)
  c2 = count_words(file2)
  print(f"Word count in {file1}: {c1}")
  print(f"Word count in {file2}: {c2}")

  # 6. Merge multiple text files into one organized study notes file
  with open(merged_file, "w", encoding="utf-8") as outfile:
    for fname in [file1, file2]:
      outfile.write(f"--- Contents of {fname} ---\n")
      with open(fname, "r", encoding="utf-8") as infile:
        outfile.write(infile.read())
        outfile.write("\n\n")

  print(f"Successfully merged '{file1}' and '{file2}' into '{merged_file}'.")


if __name__ == "__main__":
  organize_study_notes()
