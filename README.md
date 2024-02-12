# MIDI Scraper
Python script for web scraping MIDI files on the Web 

It works well on Kunstderfuge, JSBach and MIDIWorld collections. May or not may work on other collections but they can get requested and be implemented with time.
## Installation
First of all, we need to get the only dependency needed installed for the script to work.
```
pip install beautifulsoup4
```
Clone the repo or just download it manually and you're good to go ^_^
## Usage

There's two ways of using this script:
- Running it directly via CLI (WIP)
- Importing as a library into another Python file

If you want to go that way you simply need to import the MIDIScraper module in your script:
```
import midiscraper as ms
```
And then call the constructor with the desired arguments, e.g:
```
ms.MIDIScraper(url="http://www.jsbach.net/midi/midi_goldbergvariations.html", directory="midi-folder", limit=3)
```
The only necessary argument to make the call is the `url` as the `directory` and `limit` parameters have default values of "dataset" and "5" respectively.

Setting the `limit` parameter to 0 will download all MIDI files found in the Web page.

  

