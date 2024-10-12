# 11ZPE  
**Integration of Polish Educational Platform (ZPE) with Audio Description**

### Technologies used:  
- **ZPE.gov.pl API calls**  
- **ElevenLabs API calls**

The demo was deployed on the ZPE platform, but due to time constraints and very limited information about posting media to the platform, I was unable to complete it. However, I am confident that it is possible to accomplish.

Another part that requires a change is the `voiceId`. For now, the demo is using "Damian PL", and also model was changed to eleven_multilingual_v2 for Polish language generation.

The project's objective is to dynamically create a widget or audio player iframe.  
The Proof of Concept (PoC) was created in Python, but I know it can be done using a JavaScript function added to the platform (although I haven't figured out how to implement it yet). The platform is capable of operating at the API level. Unfortunately, the only information I have about the API was gathered through experimenting with API calls.

I know that the document (text value) can be fetched via an API call (as shown in the code). After fetching the text from an article, we can create an audio-description file.  
The main constraint for me is the very limited documentation. I am not sure if it's possible to inject the MP3 file into the body of the website while it's open. There are Rich Media Objects (both static and dynamic) described in the docs, but the file must first be uploaded to the platform's database/storage.

I see the potential of this project, as it will enhance and accelerate the learning process for many children.  
I hope you're also aware of this platform and its richness.  
The last thing I wanted to mention is that even if I don't win any prizes, I will pursue our government, especially the Education Department, to include this kind of accessibility enhancement in the platform.
