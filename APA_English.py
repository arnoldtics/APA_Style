def author():
    last_name = (input("Last name: ").lower()).title().strip()
    first_name = (input("First name: ").upper()).strip().split()

    if len(first_name) > 1:
        initials = ""
        for word in first_name:
            initials += word[0]+". "
        return f"{last_name}, {initials[:-2]}.,"
    else:
        return "{last_name}, {first_name[0][0]}.,"

def book():
    authors = " ".join(sorted([author() for i in range(int(input("How many authors does the book have? ")))]))
    if authors[-1] == ",": authors = authors[:-1]

    title = input("Title: ").strip()
    year = input("Year: ").strip()
    publisher = input("Publisher: ").strip()

    return print(f"\nThe title of the work is in italics\n{authors} ({year}). {title}. {publisher}.")

def website():
    authors = " ".join(sorted([author() for i in range(int(input("How many authors does the website have? ")))]))
    if authors[-1] == ",": authors = authors[:-1]

    article_title = input("Article title: ").strip()
    website_name = input("Website name: ").strip()
    last_accessed_date = input("Last accessed date: ").strip()
    link = input("Link: ").strip()

    return print(f"\nThe article title is in italics\n{authors} {article_title}. {website_name}. Last accessed on {last_accessed_date} from {link}")

if __name__ == "__main__":
    while True:
        option = input("\n1. Book citation\n2. Website citation\n3. Close program\n\n").strip()
        if option == "1": book()
        elif option == "2": website()
        elif option == "3": break
        else: print("Invalid option")