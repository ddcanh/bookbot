import sys 

from stats import get_characters_times, get_num_words, sort_dict_by_value

def main():
  if (len(sys.argv) < 2):
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
    return
  print('============ BOOKBOT ============')
  path = sys.argv[1]
  print(f'Analyzing book found at {path}...')
  print('----------- Word Count ----------')
  get_num_words(path)
  print('--------- Character Count --------')
  dict = get_characters_times(path)
  sorted_dict = sort_dict_by_value(dict)
  for key, value in sorted_dict.items():
    print(f'{key}: {value}')
  print('============= END ===============')

main()
