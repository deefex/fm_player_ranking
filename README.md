# FM Player Ranking
A method of assessing players for a particular position/role in Football Manager 2024

## Background
The original idea and raw python code for doing all the rankings for each of the 85 roles in football manager was 
written by [squirrel_plays](https://www.youtube.com/@squirrel_plays_fof4318). The raw calculations can be viewed 
[here](https://squirrelplays.neocities.org/). This merely provides a web interface wrapper making it accessible
to those that wish to take advantage of it.

The sterling folks [Fatheed7](https://github.com/Fatheed7) and [HarrisonRClark](https://github.com/HarrisonRClark)
have produced a much slicker version of this that's hosted [here](https://fm-recruitment-2ac38cc99aa0.herokuapp.com/)
and after using it a couple of times, loved their approach to dealing with 85 selectable options while confirming and
restricting what the user could choose so the resultant table wasn't stupidly wide and impractical, so I endeavoured 
to take a similar approach but write my own cumbersome code to supplement it. I don't intend to host this anywhere, but
you are of course free to download and use as is your wish.

So why write this when there's a slicker version out there? I just wanted to see if I could, plus I wanted to customise
the generated table, so I could focus down on the stats that I was interested in, making the table contents easier to 
consume visually.

## Installation
On the command line:

- Clone the repository to your machine
- `cd fm_player_ranking`
- `. ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python app.py`

## Usage
- Navigate to http://127.0.0.1:8000 in your browser
- Upload your FM24 HTML file (be sure to have used the views mentioned by squirrel_plays - downloadable [here](https://www.mediafire.com/file/ymf6xhw0bk4enjj/FM24_files.zip/file))
- Select at least one role from the list (maximum of 8)
- Click upload
- Voila!

## Todo
- Write some tests!
- Move away from the dev server
- Turn off debugger
- Table styling - column highlighting in conjunction with the current bootstrap styling?

