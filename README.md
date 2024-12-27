# AI-Driven Political Persuasion Campaigns

This project explores the generation of AI-driven manipulative video content aimed at influencing public opinion. Using GPT-4o, it generates persuasive narratives tailored to specific demographic factors such as digital literacy, cognitive reflection, and motivated reasoning. These narratives are crafted into video-based content to study the effectiveness and ethical implications of AI-driven political persuasion.

## Repository Contents

- **Prompt.py**  
  Handles the crafting and adjustment of prompts for large language models (LLMs), crucial for zero-shot or fine-tuned content generation related to political narratives.
  
- **checkpoint.json**  
  Stores the progress tracking for processed paragraphs, used to maintain checkpoints for large text data processing and ensure consistent progress across sessions.

- **Clean.py**  
  Python script to clean and preprocess text data for input into the models, ensuring data consistency and removing unwanted noise for effective downstream processing.

- **imageGPT.py**  
  Script responsible for generating images via GPT-based models, allowing for the creation of visual assets that support the persuasive narratives developed within the project.

- **midJourney.py**  
  Automates image generation with Midjourney, creating culturally relevant and impactful visuals to enhance the messaging within the political campaigns.

- **imageDict.json**  
  Contains mappings and URLs for images generated and used within the project, organized by unique identifiers.

- **mapping.json**  
  Provides mapping between unique identifiers and their respective attribute values or references, essential for cross-referencing image assets and data points.
  
- **elevenLabs.py**  
  This script interfaces with 11Labs API for generating culturally relevant audio content through voice cloning. It allows for the creation of authentic audio tailored to the audience's linguistic and cultural context.

- **uploadAudios.py**  
  Script to upload generated audio files to cloud storage, facilitating smooth integration into the video production workflow and ensuring accessible storage for multimedia assets.

- **flikiNew.py**  
  Manages the integration of multimedia components, specifically stitching together audio, video, and textual elements into cohesive video outputs using Flicki.


