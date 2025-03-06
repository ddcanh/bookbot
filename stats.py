def get_num_words(path):
  with open(path, 'r') as file:
    file_contents = file.read()
    num_words = len(file_contents.split())
    print(f'Found {num_words} total words')

def get_characters_times(path):
  with open(path, 'r') as file:
    file_contents = file.read().lower()
    char_dict = {}
    for char in file_contents:
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1
    return char_dict
   
def sort_dict_by_value(dict):
  return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}