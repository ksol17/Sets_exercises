def display_artworks(artworks):
    print("Indexed Artwork Catalog: ")
    for index, artwork, in enumerate(artworks, start=1):
        print(f"{index}. {artwork}")


artworks = {"The Starry Night", "Mona Lisa", "The Night Watch", "Guernica"}
while True:
    print("\n1. Display Artworks")
    print("2. Exit")
    choice =  input("Enter your choice: ")

    if choice == '1':
        display_artworks(artworks)
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please try again.")