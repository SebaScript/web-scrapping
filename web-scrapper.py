from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

URL_BASE = "https://www.goodreads.com"
PAGINA_1 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=1"
PAGINA_2 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=2"
PAGINA_3 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=3"


def urls_libros():
    lista_urls = []
    try:
        urls_1 = urlopen(PAGINA_1)
        urls_2 = urlopen(PAGINA_2)
        urls_3 = urlopen(PAGINA_3)
    except HTTPError as e:
        print("grave")
        return None

    sopa_1 = BeautifulSoup(urls_1.read(), features="html.parser")
    sopa_2 = BeautifulSoup(urls_2.read(), features="html.parser")
    sopa_3 = BeautifulSoup(urls_3.read(), features="html.parser")

    for url in sopa_1.findAll('a', {"class": "bookTitle"}):
        enlace = url.get('href')
        lista_urls.append(enlace)

    for url in sopa_2.findAll('a', {"class": "bookTitle"}):
         enlace = url.get('href')
         lista_urls.append(enlace)

    for url in sopa_3.findAll('a', {"class": "bookTitle"}):
         enlace = url.get('href')
         lista_urls.append(enlace)

    return lista_urls


urls = ['/book/show/2657.To_Kill_a_Mockingbird', '/book/show/72193.Harry_Potter_and_the_Philosopher_s_Stone', '/book/show/1885.Pride_and_Prejudice', '/book/show/48855.The_Diary_of_a_Young_Girl', '/book/show/170448.Animal_Farm', '/book/show/157993.The_Little_Prince', '/book/show/61439040-1984', '/book/show/4671.The_Great_Gatsby', '/book/show/5107.The_Catcher_in_the_Rye', '/book/show/33.The_Lord_of_the_Rings', '/book/show/19063.The_Book_Thief', '/book/show/10210.Jane_Eyre', '/book/show/11127.The_Chronicles_of_Narnia', '/book/show/7624.Lord_of_the_Flies', '/book/show/18135.Romeo_and_Juliet', '/book/show/136251.Harry_Potter_and_the_Deathly_Hallows', '/book/show/77203.The_Kite_Runner', '/book/show/3636.The_Giver', '/book/show/370493.The_Giving_Tree', '/book/show/24178.Charlotte_s_Web', '/book/show/1934.Little_Women', '/book/show/2767052-the-hunger-games', '/book/show/5907.The_Hobbit', '/book/show/890.Of_Mice_and_Men', '/book/show/13079982-fahrenheit-451', '/book/show/23772.Green_Eggs_and_Ham', '/book/show/5.Harry_Potter_and_the_Prisoner_of_Azkaban', '/book/show/6185.Wuthering_Heights', '/book/show/24213.Alice_s_Adventures_in_Wonderland_Through_the_Looking_Glass', '/book/show/5297.The_Picture_of_Dorian_Gray', '/book/show/1617.Night', '/book/show/18405.Gone_with_the_Wind', '/book/show/1923820.The_Holy_Bible', '/book/show/6.Harry_Potter_and_the_Goblet_of_Fire', '/book/show/386162.The_Hitchhiker_s_Guide_to_the_Galaxy', '/book/show/1420.Hamlet', '/book/show/1.Harry_Potter_and_the_Half_Blood_Prince', '/book/show/2956.The_Adventures_of_Huckleberry_Finn', '/book/show/1362112.Tolkien_On_Fairy_stories', '/book/show/24280.Les_Mis_rables', '/book/show/18144590-the-alchemist', '/book/show/5479.Brave_New_World_Brave_New_World_Revisited', '/book/show/7144.Crime_and_Punishment', '/book/show/4667024-the-help', '/book/show/2998.The_Secret_Garden', '/book/show/929.Memoirs_of_a_Geisha', '/book/show/100915.The_Lion_the_Witch_and_the_Wardrobe', '/book/show/1381.The_Odyssey', '/book/show/5326.A_Christmas_Carol', '/book/show/233093.The_Cat_in_the_Hat', '/book/show/231804.The_Outsiders', '/book/show/320.One_Hundred_Years_of_Solitude', '/book/show/128029.A_Thousand_Splendid_Suns', '/book/show/18114322-the-grapes-of-wrath', '/book/show/8127.Anne_of_Green_Gables', '/book/show/30119.Where_the_Sidewalk_Ends', '/book/show/7126.The_Count_of_Monte_Cristo', '/book/show/375802.Ender_s_Game', '/book/show/19543.Where_the_Wild_Things_Are', '/book/show/52892857-the-color-purple', '/book/show/24583.The_Adventures_of_Tom_Sawyer', '/book/show/1953.A_Tale_of_Two_Cities', '/book/show/4214.Life_of_Pi', '/book/show/38447.The_Handmaid_s_Tale', '/book/show/332613.One_Flew_Over_the_Cuckoo_s_Nest', '/book/show/35031085-frankenstein', '/book/show/191139.Oh_the_Places_You_ll_Go_', '/book/show/15823480-anna-karenina', '/book/show/6900.Tuesdays_with_Morrie', '/book/show/99107.Winnie_the_Pooh', '/book/show/4981.Slaughterhouse_Five', '/book/show/2165.The_Old_Man_and_the_Sea', '/book/show/168668.Catch_22', '/book/show/12296.The_Scarlet_Letter', '/book/show/8852.Macbeth', '/book/show/34.The_Fellowship_of_the_Ring', '/book/show/41865.Twilight', '/book/show/7604.Lolita', '/book/show/485894.The_Metamorphosis', '/book/show/49552.The_Stranger', '/book/show/52036.Siddhartha', '/book/show/18619684-the-time-traveler-s-wife', '/book/show/32929.Goodnight_Moon', '/book/show/15881.Harry_Potter_and_the_Chamber_of_Secrets', '/book/show/656.War_and_Peace', '/book/show/14891.A_Tree_Grows_in_Brooklyn', '/book/show/114345.The_Little_House_Collection', '/book/show/41817486-a-clockwork-orange', '/book/show/355697.All_Quiet_on_the_Western_Front', '/book/show/149267.The_Stand', '/book/show/3836.Don_Quixote', '/book/show/46787.Uncle_Tom_s_Cabin', '/book/show/646462._', '/book/show/662.Atlas_Shrugged', '/book/show/4934.The_Brothers_Karamazov', '/book/show/7244.The_Poisonwood_Bible', '/book/show/13214.I_Know_Why_the_Caged_Bird_Sings', '/book/show/153747.Moby_Dick_or_The_Whale', '/book/show/323355.The_Book_of_Mormon', '/book/show/968.The_Da_Vinci_Code', '/book/show/2623.Great_Expectations', '/book/show/1078.The_Good_Earth', '/book/show/561909.The_Hiding_Place', '/book/show/17245.Dracula', '/book/show/33574273-a-wrinkle-in-time', '/book/show/11870085-the-fault-in-our-stars', '/book/show/39988.Matilda', '/book/show/22628.The_Perks_of_Being_a_Wallflower', '/book/show/5129.Brave_New_World', '/book/show/14935.Sense_and_Sensibility', '/book/show/21787.The_Princess_Bride', '/book/show/1371.The_Iliad', '/book/show/4406.East_of_Eden', '/book/show/10365.Where_the_Red_Fern_Grows', '/book/show/391729.The_Tell_Tale_Heart_and_Other_Writings', '/book/show/4069.Man_s_Search_for_Meaning', '/book/show/7784.The_Lorax', '/book/show/6148028-catching-fire', '/book/show/13496.A_Game_of_Thrones', '/book/show/1618.The_Curious_Incident_of_the_Dog_in_the_Night_Time', '/book/show/285500.The_Declaration_of_Independence_The_Constitution_of_the_United_States', '/book/show/76620.Watership_Down', '/book/show/6514.The_Bell_Jar', '/book/show/6310.Charlie_and_the_Chocolate_Factory', '/book/show/17899948-rebecca', '/book/show/44767458-dune', '/book/show/2318271.The_Last_Lecture', '/book/show/16299.And_Then_There_Were_None', '/book/show/144974.The_Velveteen_Rabbit', '/book/show/2122.The_Fountainhead', '/book/show/12232938-the-lovely-bones', '/book/show/13023.Alice_in_Wonderland', '/book/show/1852.The_Call_of_the_Wild', '/book/show/2429135.The_Girl_with_the_Dragon_Tattoo', '/book/show/838729.The_Return_of_the_King', '/book/show/5472.Animal_Farm_1984', '/book/show/3431.The_Five_People_You_Meet_in_Heaven', '/book/show/343.Perfume', '/book/show/58913358-a-story-of-yesterday', '/book/show/252577.Angela_s_Ashes', '/book/show/236093.The_Wonderful_Wizard_of_Oz', '/book/show/61215372-the-two-towers', '/book/show/310259.Love_You_Forever', '/book/show/40940121-bridge-to-terabithia', '/book/show/6656.The_Divine_Comedy', '/book/show/6288.The_Road', '/book/show/4473.A_Prayer_for_Owen_Meany', '/book/show/1622.A_Midsummer_Night_s_Dream', '/book/show/2156.Persuasion', '/book/show/119073.The_Name_of_the_Rose', '/book/show/2547.The_Prophet', '/book/show/7190.The_Three_Musketeers', '/book/show/119322.The_Golden_Compass', '/book/show/43641.Water_for_Elephants', '/book/show/39999.The_Boy_in_the_Striped_Pajamas', '/book/show/5043.The_Pillars_of_the_Earth', '/book/show/113946.How_the_Grinch_Stole_Christmas_', '/book/show/71728.Jonathan_Livingston_Seagull', '/book/show/18254.Oliver_Twist', '/book/show/37435.The_Secret_Life_of_Bees', '/book/show/33648131-the-notebook', '/book/show/117833.The_Master_and_Margarita', '/book/show/7260188-mockingjay', '/book/show/188572.The_Complete_Sherlock_Holmes', '/book/show/168642.In_Cold_Blood', '/book/show/17250.The_Crucible', '/book/show/4989.The_Red_Tent', '/book/show/1232.The_Shadow_of_the_Wind', '/book/show/4900.Heart_of_Darkness', '/book/show/9712.Love_in_the_Time_of_Cholera', '/book/show/7445.The_Glass_Castle', '/book/show/143534.The_Gift_of_the_Magi', '/book/show/19501.Eat_Pray_Love', '/book/show/9717.The_Unbearable_Lightness_of_Being', '/book/show/43763.Interview_with_the_Vampire', '/book/show/10534.The_Art_of_War', '/book/show/2696.The_Canterbury_Tales', '/book/show/70401.On_the_Road', '/book/show/21348.Aesop_s_Fables', '/book/show/8130077-the-screwtape-letters', '/book/show/30.J_R_R_Tolkien_4_Book_Boxed_Set', '/book/show/51496.Dr_Jekyll_and_Mr_Hyde', '/book/show/22034.The_Godfather', '/book/show/36236124-fight-club', '/book/show/16902.Walden', '/book/show/7733.Gulliver_s_Travels', '/book/show/2932.Robinson_Crusoe', '/book/show/22463.The_Origin_of_Species', '/book/show/16981.Invisible_Man', '/book/show/6969.Emma', '/book/show/28862.The_Prince', '/book/show/10959.Sophie_s_World', '/book/show/22917.The_Complete_Grimm_s_Fairy_Tales', '/book/show/2493.The_Time_Machine', '/book/show/17690.The_Trial', '/book/show/472331.Watchmen', '/book/show/19380.Candide', '/book/show/546018.Roots', '/book/show/6149.Beloved', '/book/show/6867.Atonement', '/book/show/61215351-the-fellowship-of-the-ring', '/book/show/46799.Go_Ask_Alice', '/book/show/84981.Tuck_Everlasting', '/book/show/10917.My_Sister_s_Keeper', '/book/show/133518.The_Things_They_Carried', '/book/show/13335037-divergent', '/book/show/350.Stranger_in_a_Strange_Land', '/book/show/3876.The_Sun_Also_Rises', '/book/show/402045.The_Mists_of_Avalon', '/book/show/40792344-mere-christianity', '/book/show/28187.The_Lightning_Thief', '/book/show/378.The_Phantom_Tollbooth', '/book/show/19321.The_Tale_of_Peter_Rabbit', '/book/show/853510.Murder_on_the_Orient_Express', '/book/show/15195.The_Complete_Maus', '/book/show/47281.Number_the_Stars', '/book/show/89959.U_S_Constitution_Saddlewire_', '/book/show/6689.James_and_the_Giant_Peach', '/book/show/76401.Bury_My_Heart_at_Wounded_Knee', '/book/show/13.The_Ultimate_Hitchhiker_s_Guide_to_the_Galaxy', '/book/show/375013.Schindler_s_List', '/book/show/92057.The_Autobiography_of_Malcolm_X', '/book/show/3008.A_Little_Princess', '/book/show/43070.The_Essential_Calvin_and_Hobbes', '/book/show/2187.Middlesex', '/book/show/49436.Three_Cups_of_Tea', '/book/show/60748.A_Child_Called_It_', '/book/show/1845.Into_the_Wild', '/book/show/27494.Leaves_of_Grass', '/book/show/37415.Their_Eyes_Were_Watching_God', '/book/show/5659.The_Wind_in_the_Willows', '/book/show/439288.Speak', '/book/show/34268.Peter_Pan', '/book/show/30289.The_Republic', '/book/show/2767.A_People_s_History_of_the_United_States', '/book/show/30165203-american-gods', '/book/show/38709.Holes', '/book/show/821611.The_Story_of_My_Life', '/book/show/7069.The_World_According_to_Garp', '/book/show/99561.Looking_for_Alaska', '/book/show/514811.The_Secret_Magdalene', '/book/show/12067.Good_Omens', '/book/show/8921.The_Hound_of_the_Baskervilles', '/book/show/37781.Things_Fall_Apart', '/book/show/21.A_Short_History_of_Nearly_Everything', '/book/show/58572970-the-addiction-manifesto', '/book/show/3869.A_Brief_History_of_Time', '/book/show/41044096-island-of-the-blue-dolphins', '/book/show/40937505', '/book/show/135479.Cat_s_Cradle', '/book/show/10799.A_Farewell_to_Arms', '/book/show/46306.The_Complete_Fairy_Tales', '/book/show/40495148-blindness', '/book/show/5148.A_Separate_Peace', '/book/show/264158.The_Raven', '/book/show/1812457.The_Shack', '/book/show/9375.Fried_Green_Tomatoes_at_the_Whistle_Stop_Cafe', '/book/show/2175.Madame_Bovary', '/book/show/14743.The_God_Delusion', '/book/show/7763.The_Joy_Luck_Club', '/book/show/67896.Tao_Te_Ching', '/book/show/27712.The_Neverending_Story', '/book/show/228560.Sophie_s_Choice', '/book/show/310612.A_Confederacy_of_Dunces', '/book/show/4865.How_to_Win_Friends_and_Influence_People', '/book/show/960.Angels_Demons', '/book/show/6334.Never_Let_Me_Go', '/book/show/1842.Guns_Germs_and_Steel', '/book/show/4588.Extremely_Loud_Incredibly_Close', '/book/show/6801755-flow-down-like-silver', '/book/show/40611463-the-clan-of-the-cave-bear', '/book/show/32261.Tess_of_the_D_Urbervilles', '/book/show/373115.The_Color_Purple', '/book/show/10964.Outlander', '/book/show/48757.The_Tao_of_Pooh', '/book/show/36072.The_7_Habits_of_Highly_Effective_People', '/book/show/428263.Eclipse', '/book/show/17125.One_Day_in_the_Life_of_Ivan_Denisovich', '/book/show/30118.A_Light_in_the_Attic', '/book/show/338798.Ulysses', '/book/show/256008.Lonesome_Dove', '/book/show/41681.The_Jungle', '/book/show/480204.The_Phantom_of_the_Opera', '/book/show/1162543.Breaking_Dawn', '/book/show/1869.Nickel_and_Dimed', '/book/show/15997.Paradise_Lost', '/book/show/186074.The_Name_of_the_Wind', '/book/show/7779.Horton_Hears_a_Who_', '/book/show/9777.The_God_of_Small_Things', '/book/show/11566.The_Green_Mile', '/book/show/37732.Are_You_There_God_It_s_Me_Margaret', '/book/show/32087.All_Creatures_Great_and_Small_All_Things_Bright_and_Beautiful', '/book/show/295.Treasure_Island', '/book/show/9328.The_House_of_the_Spirits', '/book/show/11588.The_Shining', '/book/show/1375.The_Iliad_The_Odyssey', '/book/show/5805.V_for_Vendetta', '/book/show/46654.The_Foundation_Trilogy', '/book/show/569564.The_Complete_Works', '/book/show/49041.New_Moon']


def info_libros():
    info = []
    for url in urls:
        libro = urlopen(URL_BASE+url)
        libro_sopa = BeautifulSoup(libro.read(), features="html.parser")
        titulo = libro_sopa.find("h1").string

        try:
            autor = libro_sopa.find("span", {"class": "ContributorLink__name"}).string
        except:
            autor = "unknown"

        try:
            fecha = libro_sopa.find("p", {"data-testid": "publicationInfo"}).string.strip("First published ")
        except:
            fecha = "unknown"

        boton_precio = libro_sopa.find("button", {"class": "Button Button--buy Button--medium Button--block"})

        try:
            precio = boton_precio.find("span", {"class": "Button__labelItem"}).string.split("$")[1]
        except:
            precio = 0

        try:
            calificacion = libro_sopa.find("div", {"class": "RatingStatistics__rating"}).string
        except:
            calificacion = "unknown"

        try:
            botones_genero = libro_sopa.find_all("span", {"class": "BookPageMetadataSection__genreButton"})

            c = 0
            generos = []
            for boton in botones_genero:
                if c == 3 or not botones_genero:
                    break
                genero = boton.find("span", {"class": "Button__labelItem"}).string
                generos.append(genero)
                c += 1

        except:
            generos = ["unknown"]

        libro_info = {
            "titulo": titulo,
            "autor": autor,
            "fecha": fecha,
            "precio": precio,
            "calificacion": calificacion,
            "generos": generos
        }

        info.append(libro_info)

    with open("libros.json", "w") as libros_json:
        json.dump(info, libros_json, indent=4)


info_libros()
