# Picture-and-Video-Searcher
This is a basic example of how an algorithm that searches for pictures and videos might work. 

I often find interesting videos/pictures on the internet that make me want to watch the shows that they came from, but sometimes the videos/pictures don't have any names posted alongside them. Even looking for them on Google doesn't help very much because you can't find something unless you know its name. So i thought about developing a way to find any videos/pictures online even if you don't know what they're called. this isn't very effective since its a basic example of what I think a video/picture search algorithm would look like.

Frames2Base64 takes any picture and turns it into base64, it can also take a video and turn it's individual frames into base64. It then pastes the resulting base64 string into a text file.
SEARCHER takes a video/picture and turns it into base64 and looks for a match among a group of text files and returns the name of the text file that matches your search.

Imagine a streaming service such as Netflix. they could use Frames2Base64 to turn all their shows into text and store them in a database. Whenever someone encounters one of their shows on the internet but they don't know what its called they could use SEARCHER to look for it in the database and find the show easily. This idea could work for other platforms as well such as Youtube.

LIMITATIONS

Turning each frame in a video to base64 and pasting it in a text file is very impractical, as the resulting text file takes up a lot of space. I did it for a 1.97 MB video and the resulting text file was 31.9 MB. I can't imagine what the result would be for bigger videos. 
