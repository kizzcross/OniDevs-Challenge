# Technical Explananation

## Classes/Script Files
- ``Models.py``: contain the models for "Artist" and "Music" classes which contain the function "getMusicsOfArtist" that gets us the dict that is used in the csv exportation.
- ``export_csv.py``: contain an export-csv function that build the csv based on the data of music and artists.
- ``admin.py``: register the functions and models to the Django admin for example "Artist", "Music" and "export_csv".
- ``forms.py``: responsible for the adequation of the form.

## Routes
- ``/<int:id>/``: Route for Music Update.
- ``/delete/<int:id>/``: Route for music delete.
- ``/list/``: Route for the music list.

## Why use docker
- For better management of the development envroiment, without any problems between the reviewer and reviewed.

## My problems/difficulties
- Getting the dict list and the csv exportation was the hardest part, for that I thank my friend Luis "Rastrian" Vaz for the contribuition.

## Contribuitors

Thank to all contribuitors:
<table>
    <td align="center"><a href="https://github.com/Rastrian"><img src="https://avatars.githubusercontent.com/u/68169692?s=460&u=18d8c83d147b111b2aa87dc8ae228500b3105d85&v=4" width="100px;" alt="Joao Victor (kizzcross)"/><br /><sub><b>Joao Victor (kizzcross)</b></sub></a></td>
    <td align="center"><a href="https://github.com/Rastrian"><img src="https://avatars1.githubusercontent.com/u/10719452?s=460&u=2b0a8731d7344b952690f2982b5e5b481ceeee60&v=4" width="100px;" alt="Luis Vaz (Rastrian)"/><br /><sub><b>Luis Vaz (Rastrian)</b></sub></a></td>
</table>

## Images
<img src="https://github.com/kizzcross/OniDevs-Challenge/blob/master/assets/1.png?raw=true" alt="Initial Form" />
<img src="https://github.com/kizzcross/OniDevs-Challenge/blob/master/assets/2.png?raw=true" alt="List of musics" />
<img src="https://github.com/kizzcross/OniDevs-Challenge/blob/master/assets/3.png?raw=true" alt="Update Form" />
<img src="https://github.com/kizzcross/OniDevs-Challenge/blob/master/assets/4.png?raw=true" alt="Function in Python-Admin to export Artist Musics to excel file (csv)" />