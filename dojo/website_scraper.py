city = "Hong Kong"
area = "sai ying pun"
link = "https://www.sassyhongkong.com/living-neighbourhood-guide-sai-ying-pun/"

genre = ["area-guide", "beach", "comedy", "hike", "food"]


data = {
    "city": city,
    "area": area,
    "genre": input("Article Genre: "),
    "is_list": input("Is It A List: "),
    "link": link,
    "website": link.split("www.")[1].split(".")[0],
}
