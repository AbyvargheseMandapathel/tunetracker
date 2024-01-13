# Tune Tracker

The Favourite Songs Django Application is designed to allow users to manage and showcase their favorite songs, including information about the artists who perform them.


## Environment Setup and Project Execution

1. Clone the Repository
2. Create a Virtual Environment (Recommended)
``` bash
python -m venv venv
```
3. Activate the Virtual Environment

  On Windows:

``` bash
.\venv\Scripts\activate
```
On macOS/Linux:
``` bash
source venv/bin/activate
```
4. Install Packages
``` bash
pip install -r requirements.txt
```
5.Navigate to the Project Directory
``` bash
cd FavoriteTunes
```

6.Run Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```

6.Run server
``` bash
python manage.py runserver
```
# Screenshots
1. Dashboard
![Dashboard](screenshots/dashboard.png)

2.Artists
![Artist](screenshots/Artists.png)

3. Songs
![Songs](screenshots/Songs.png)

4. Video Player
![Video Player](screenshots/vd.png)

5. Add Song
![Add Song](screenshots/addsong.png)

6. Add Artist
![Add Artist](screenshots/addartist.png)

7. Song Detail
![Song Detail](screenshots/songdetail.png)

8.Artist Details
![Artist Details](screenshots/artistdetail.png)


# Note

In case if youtube embed is showing "Video not available" try accessing the application via 

```bash
  http://localhost:8000/
```
  Reference : https://stackoverflow.com/a/56419165/12655561
