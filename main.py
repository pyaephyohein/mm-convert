import myanmar.encodings
import myanmar.converter

def main():
    text = input("Unicode Here >>>  ")
    conv = myanmar.converter.convert(text,'unicode','zawgyi')
    print(f'Zawgyi is >>>{conv}')

if __name__=="__main__":
    main()

