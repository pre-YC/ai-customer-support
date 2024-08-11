from openaiclient import OpenAIClient
from prompts.template import PromptTemplate
from openai import OpenAI

import argparse
import json
import jinja2
import time


class ScriptGenerator:
    """
    This class is responsible for generating the script for the user knowing the world choice, input twist.
    world_choice: str
    This is the world choice for the user, like Harry Potter.
    input_twist: str
    This is the input of the user to have a twist in the story.
    """

    def __init__(self, world_choice, input_twist):
        self.world_choice = world_choice
        self.input_twist = input_twist
        self.oac = OpenAIClient()

    def define_characters(self):
        """
        This function is responsible for defining the characters in the story.
        """

        prompt_template = PromptTemplate("prompts/characters.jinja")
        prompt = prompt_template.render(
            world_choice=self.world_choice,
            input_twist=self.input_twist,
        )
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
        completion = self.oac.chat(messages, json_mode=True)
        response = json.loads(completion)
        return response

    def generate_general_story(self, characters):
        user_prompt = "You are a famous movie director known for writing engaging stories with dramatic dialogue. You need to generate a story for a scene based on the world choice and input twist provided by the user. \n"
        user_prompt += f"Can you generate a general story outline of what could happen in a short scene in the world of {self.world_choice} with the twist that {self.input_twist}? Pick a scene that involves only the characters {characters}. Don't change the name of the characters even if the twist implies a change. Follow the structure of a scene and make sure there is good amount of dialogue between characters."

        system_prompt = PromptTemplate("prompts/story_structure.jinja").render()
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        result = self.oac.chat(messages, False, temperature=0.8)

        print("##### STORY ###### \n\n", result, "\n\n")
        return result

    def get_setting(self, story):
        """
        This function is responsible for getting the general description of the story.
        """
        user_prompt = "You are a famous director known for writing engaging stories with beautiful settings. You have access to a story and your job is to generate a general setting for the scene. Include location, background, weather, mood and other details you can think of. \n"
        user_prompt += f"Here's the story: \n\n {story}"
        messages = [
            {"role": "user", "content": user_prompt},
        ]
        result = self.oac.chat(messages, False, temperature=1)

        print("##### SETTING ###### \n\n", result, "\n\n")
        return result

    def generate_script(self, characters, story):
        """
        This function is responsible for generating the script for the user.
        description: str
        This is the description of the scene.
        characters: dict
        This is the dictionary of the characters in the story.
        user_character: str
        This is the user character in the story.
        """
        prompt_template = PromptTemplate("prompts/write_script.jinja")
        prompt = prompt_template.render(
            world_choice=self.world_choice,
            input_twist=self.input_twist,
            characters=characters,
            story=story,
        )
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
        completion = self.oac.chat(messages, json_mode=True)
        response = json.loads(completion)

        print("#####  script ##### \n\n", response, "\n\n")

        return response

    def final_script(self):

        characters = self.define_characters()

        story = self.generate_general_story(characters)

        setting = self.get_setting(story)

        script = self.generate_script(characters=characters, story=story)

        data_to_save = {
            "scene_description": setting,
            "characters": characters,
            "dialogue": script,
        }
        print("DATA TO SAVE\n\n")
        print(data_to_save)
        print("\n\n")

        with open("script_data.json", "w") as json_file:
            json.dump(data_to_save, json_file, indent=4)

        print("Generated script saved to script_data.json")

        return data_to_save


def main():
    parser = argparse.ArgumentParser(description="Generate a script for the user.")
    parser.add_argument(
        "--world_choice", type=str, help="The world choice for the user."
    )
    parser.add_argument(
        "--input_twist", type=str, help="The input twist for the story."
    )
    args = parser.parse_args()
    world_choice = args.world_choice
    input_twist = args.input_twist
    script_generator = ScriptGenerator(world_choice, input_twist)

    description = script_generator.get_setting()

    characters = script_generator.define_characters()
    user_input = input(
        f"Characters: {characters}\nWhich character do you want to play? Select 1 or 2, then press enter to continue.\n ======>  "
    )
    user_character = characters.get(f"character{user_input}")["name"]

    script = script_generator.generate_script(
        characters=characters, user_character=user_character, description=description
    )

    data_to_save = {
        "scene_description": description,
        "characters": characters,
        "dialogue": script,
    }

    with open("script_data.json", "w") as json_file:
        json.dump(data_to_save, json_file, indent=4)

    print("Generated script saved to script_data.json")


if __name__ == "__main__":
    main()
