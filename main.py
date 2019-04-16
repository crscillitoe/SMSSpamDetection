import features
from data_loader import load_data

def main():
    file_path = 'spam.csv'
    data = load_data(file_path)

    print(data)

if __name__ == '__main__':
    main()
