import json
import math
import folium

from urllib.request import urlopen
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)

print(data)


m = folium.Map(location=[12.869292, 74.922438], zoom_start=15)


folium.Marker([12.866334, 74.924229],
              popup="<h1>sahyadri college of engineering and manegment </h1><img src='1524131579phpsbmi2K.png' width=400px><p>good option for education </p>",
              tooltip='sahyadri college ',
              icon=folium.Icon(color='red')).add_to(m)
folium.Marker([12.870958267878613, 74.89615723887104],
              popup="<h1>Adyar Plaza Inn </h1> <img src=' 282934500.jpg' width=400px<p> good option  for lunch</p> ",
              tooltip='adyar plaza ',
              icon=folium.Icon(icon='hotel'), icon_color='red').add_to(m)

folium.Circle([12.868184, 74.914056],
              radius=2100,
              popup='adyar',
              colour='blue',
              fill=True,
              fill_colour="blue"
              ).add_to(m)
folium.Marker([12.867554404040758, 74.91675584251549],
              popup="<h1>SHETTY LUNCH HOME ADYAR</h1><img src='550a3932-cfaf-4888-8b38-91ee89275332.jpg' width=400px><p>soup,seafood,asian,diner </p>",
              tooltip='SHETTY LUNCH HOME',
              icon=folium.Icon(icon='hotel'), icon_color='red').add_to(m)
folium.Marker([12.874040140237623, 74.92487085155025],
              popup="<h1>tandoor kitchen</h1><img src='799e0baf-fba2-4e2c-82ef-0718fc3cf6a8.jpg' width=400px><p>soup,seafood,asian,diner </p>",
              tooltip='tandoor kitchen',
              icon=folium.Icon(icon='hotel'), icon_color='red').add_to(m)

folium.Marker([12.869240003606938, 74.92048417429064],
              popup="<h1>Ayaaf's Kitchen </h1><img src='5b07caca-94d6-48f6-8e37-9e9e55d784c5.jpg' width=100px><p>u can order in my website</p>",
              tooltip="Ayaaf's Kitchen",
              icon=folium.Icon(icon='hotel'), icon_color='BLUE').add_to(m)

folium.Marker([12.870337882847247, 74.92232997539874],
              popup="<h1>HOTEL VAARIDHI</h1><img src='60fcb5b7-da71-4acd-a08b-64a0c68d7832.jpg' width=400px><p>u can order in my website</p>",
              tooltip="HOTEL VAARIDHI",
              icon=folium.Icon(icon='hotel'), icon_color='red').add_to(m)

folium.Marker([12.86703, 74.92501],
              popup="<h1>Sahyadri Food Court</h1><img src='377c02f7-3eb6-48e9-b686-60086fd6a2a0.jpg' width=400px><p>u can order in my website</p>",
              tooltip="Sahyadri Food Court",
              icon=folium.Icon(icon='hotel'), icon_color='red').add_to(m)


folium.Marker([12.8675914, 74.9288305],
              popup="<h1>ORANGE JUICE DELIVERY BOY ID=OJ001</h1><img src='DELIVERY BOY.jpg' width=150px><p>u can order in my website</p>",
              tooltip="DELIVERY BOY 1",
              icon=folium.Icon(color='black')).add_to(m)

folium.Marker([12.868908, 74.899645],
              popup="<h1>ORANGE JUICE DELIVERY BOY ID=OJ002</h1><img src='DELIVERY BOY.jpg' width=150px><p>u can order in my website</p>",
              tooltip="DELIVERY BOY 2",
              icon=folium.Icon(color='black')).add_to(m)

folium.Marker([12.866730,74.903878],
              popup="<h1>ORANGE JUICE DELIVERY BOY ID=OJ003</h1><img src='DELIVERY BOY.jpg' width=150px><p>u can order in my website</p>",
              tooltip="DELIVERY BOY 3",
              icon=folium.Icon(color='black')).add_to(m)

folium.Marker([12.866127,74.909932],
              popup="<h1>ORANGE JUICE DELIVERY BOY ID=OJ004</h1><img src='DELIVERY BOY.jpg' width=150px><p>u can order in my website</p>",
              tooltip="DELIVERY BOY 4",
              icon=folium.Icon(color='black')).add_to(m)

from geopy.distance import geodesic

# Loading the lat-long data for Kolkata & Delhi
a = ("", "")
b = ("", "")
print((geodesic(a, b).km), end="km")


# Print the distance calculated in km

def hotel_1():
    z = []
    h1 = (12.870958267878613, 74.89615723887104)
    a = (12.8675914, 74.9288305)
    e = geodesic(h1, a).km
    z.append(e)
    h1 = (12.870958267878613, 74.89615723887104)
    b = (12.868908, 74.899645)
    f = geodesic(h1, b).km
    z.append(f)
    h1 = (12.870958267878613, 74.89615723887104)
    c = (12.866730, 74.903878)
    g = geodesic(h1, c).km
    z.append(g)
    h1 = (12.870958267878613, 74.89615723887104)
    d = (12.866127, 74.909932)
    h = geodesic(h1, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO Adyar plaza home he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO Adyar plaza home he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO Adyar plaza home he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO Adyar plaza home he will be ur delivery boy")
        print("\nid=OJ003 IS NEAR TO Adyar plaza home he will be ur delivery boy")


def hotel_2():
    z = []
    h2 = (12.867554404040758, 74.91675584251549)
    a = (12.8675914, 74.9288305)
    e = geodesic(h2, a).km
    z.append(e)
    h2 = (12.867554404040758, 74.91675584251549)
    b = (12.868908, 74.899645)
    f = geodesic(h2, b).km

    z.append(f)
    h2 = (12.867554404040758, 74.91675584251549)
    c = (12.866730, 74.903878)
    g = geodesic(h2, c).km

    z.append(g)
    h2 = (12.867554404040758, 74.91675584251549)
    d = (12.866127, 74.909932)

    h = geodesic(h2, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO shettys lunch home home he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO shettys lunch home home he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO shettys lunch home home he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO shettys lunch home home he will be ur delivery boy")


def hotel_3():
    z = []
    h3 = (12.874040140237623, 74.92487085155025)
    a = (12.8675914, 74.9288305)
    e = geodesic(h3, a).km

    z.append(e)
    h3 = (12.874040140237623, 74.92487085155025)
    b = (12.868908, 74.899645)
    f = geodesic(h3, b).km

    z.append(f)
    h3 = (12.874040140237623, 74.92487085155025)
    c = (12.866730, 74.903878)
    g = geodesic(h3, c).km

    z.append(g)
    h3 = (12.874040140237623, 74.92487085155025)
    d = (12.866127, 74.909932)

    h = geodesic(h3, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO tandoor kitchen home he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO tandoor kitchen home he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO tandoor kitchen home he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO tandoor kitchen he will be ur delivery boy")


def hotel_4():
    z = []
    h4 = (12.869240003606938, 74.92048417429064)
    a = (12.8675914, 74.9288305)
    e = geodesic(h4, a).km

    z.append(e)
    h4 = (12.869240003606938, 74.92048417429064)
    b = (12.868908, 74.899645)
    f = geodesic(h4, b).km

    z.append(f)
    h4 = (12.869240003606938, 74.92048417429064)
    c = (12.866730, 74.903878)
    g = geodesic(h4, c).km

    z.append(g)
    h4 = (12.869240003606938, 74.92048417429064)
    d = (12.866127, 74.909932)

    h = geodesic(h4, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO ayaaf's kitchen home he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO ayaaf's kitchen home he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO ayaaf's kitchen home he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO ayaaf's kitchen he will be ur delivery boy")


def hotel_5():
    z = []
    h5 = (12.870337882847247, 74.92232997539874)
    a = (12.8675914, 74.9288305)
    e = geodesic(h5, a).km

    z.append(e)
    h5 = (12.870337882847247, 74.92232997539874)
    b = (12.868908, 74.899645)
    f = geodesic(h5, b).km

    z.append(f)
    h5 = (12.870337882847247, 74.92232997539874)
    c = (12.866730, 74.903878)
    g = geodesic(h5, c).km

    z.append(g)
    h5 = (12.870337882847247, 74.92232997539874)
    d = (12.866127, 74.909932)

    h = geodesic(h5, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO hotel vaaridhi he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO hotel vaaridhi he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO hotel vaaridhi he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO hotel vaaridhi he will be ur delivery boy")


def hotel_6():
    z = []
    h6 = (12.86703, 74.92501)
    a = (12.8675914, 74.9288305)
    e = geodesic(h6, a).km

    z.append(e)
    h6 = (12.86703, 74.92501)
    b = (12.868908, 74.899645)
    f = geodesic(h6, b).km

    z.append(f)
    h6 = (12.86703, 74.92501)
    c = (12.866730, 74.903878)
    g = geodesic(h6, c).km

    z.append(g)
    h6 = (12.86703, 74.92501)
    d = (12.866127, 74.909932)

    h = geodesic(h6, d).km
    z.append(h)
    for i in range(0, 4):
        print(z[i], end=" ")
    x = min(z)
    print("\nminimum distance is")
    print(x,end="km")
    if x == e:
        print("\nid=OJ001 IS NEAR TO sahyadri food he will be ur delivery boy")
    elif x == f:
        print("\nid=OJ002 IS NEAR TO sahyadri food he will be ur delivery boy")
    elif x == g:
        print("\nid=OJ003 IS NEAR TO sahyadri food he will be ur delivery boy")
    else:
        print("\nid=OJ003 IS NEAR TO sahyadri food he will be ur delivery boy")


print((geodesic(a, b).km), end="km")
print("choose the restuarant number  from below :")
print(
    "1.Adyar plaza \n2.shettys lunch home \n3.tandoor kitchen \n4.ayaaf's kitchen \n5.hotel vaaridhi\n6.sahyadri food court\n")
string = int(input("enter the option "))
match string:
    case 1:
        hotel_1()
    case 2:
        hotel_2()
    case 3:
        hotel_3()
    case 4:
        hotel_4()
    case 5:
        hotel_5()
    case 6:
        hotel_6()

m.save('map.html')