## GPT-2 Short Story Generator
### How does your algorithm work? How do you generate the storyline?

My algorithm works asking the user to choose a character name and a genre for the story. It then randomly chooses one of four opening sentences which I hardcoded. They are very general opening sentences that can be the start of any story.

From there, the sentence is passed down to a pretrained gpt2 genre story generator from pranavpsv which is created by fine-tuning GPT2 on genre-based stories. It generate stories based on user inputted genre and starting prompts. The final text is then printed and also converted to an mp3 audio file.

### What topics/processes are you exploring in your work? What did you hope to achieve?

Through my work, I wanted to explore the different possibilities and outcomes that can come out. If the user inputs Batman or Mario for example as a character name, then then Bruce Wayne or Luigi would have a high chance of appearing in the generated text. The choice of name may or may not have an impact on the output.

For me, my goal was to generate stories that make sense. However, not all outputs made sense. If one output does not make sense and we refresh, the next one probably would, or the one after or after. There are a great number of possibilities.

### How does the presentation of your work shape the response of the reader?

In asking the user to enter a name and genre for the story, the program is hinting that a certain computer algorithm with be used to compute the story. The original plan was to create a html page where the background image would be the setting of the story and the with the text printing and an audio to read it aloud. It would have provided the user with visual imagery and the audio play would be a reminder that it is computer generated. However, the only thing I managed to get was the first page promting the user for input.

The colab version is also appropriate, but more messy with all the code and printouts. Yet again, it serves as a reminder that this is computer generated.

## Sample Outputs 
### Sample Output 1 - Action
Whether I shall turn out to be the hero of my own life, or whether that station will be held by anybody else, it will be determined tonight. I am Geralt of Gotham City and my time has come.

The story begins in a bank robbery, where the gangster John Wayne and his pals kill the robbers before he and the gangster escape. The criminals decide to keep the evidence against them and head to the apartment of Wayne's wife, Marge, where one of the murdered hostages is. At the apartment, Wayne finds "The Man" in the apartment's safe, but he refuses to allow Marge to confront him. While being questioned by his son and nephew, Wayne sees himself being accused and is attacked and knocked out with several objects thrown by the Man — a crowbar, a rope ladder, a hammer, a bat, a crowbar, a golf club, a rifle, a water pistol, a chain saw, and a pipe wrench. Before dying, Wayne tells Marge that there will be a price, an opportunity for revenge, and that he will meet her on the day when he and the gangster meet.

### Sample Output 2 - Horror
Once there was a– wait no. It doesn’t seem right. Okay. Once upon a tim— no it isn’t this either. Okay, time. Well how do you open up a story? I am Annabelle of Springfield and my time has come.

Story of a girl living in a small town, Annabelle. As a child little girl, she was the victim of her mother's abuse. Her father always suspected her innocence, as he kept troubling her that her family could not afford a proper education. His family would make her pay for the trouble they had caused as a result of being an underprivileged child. Story of life in a small town from a childhood with Annabelle, including her mother’s abuse.

### Sample Output 3 - Superhero
I told you last night that I might be gone sometime because I’m old and weak, and you said that was not true. I tried to lift the van last night with my pinkey and I failed. I lost all my strength. I am Willy of Dragon Stone and my time has come.

I said this to my Aunt Martha. I heard things lately that was not true, but maybe it’s just that when the weather is nice and warm, and all this time that I’m not home anymore, what comes next is your imagination. I’m going to be old, weak and woeful and it was’t all right to be old. So I thought “the tree with my pinkey, there” must be another tree. And my pinkey was just like the tree with my pinkey. I don’t know how old it was; it had nothing to do with me. That’s why I ran to the window and tried to lift the van and my pinkey didn’t work. And onlookers were asking “I wonder what could have happened to it?” And finally, what came next was my imagination about the old tree. I took the pinkey and lifted it, like a strong man lifting a strong man.
