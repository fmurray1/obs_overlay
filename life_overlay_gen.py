"""
Script generates a square image with a number in the middle 
to use as an OBS overlay for playing magic over webcam.
"""
import click
from PIL import Image, ImageDraw, ImageFont

SNOW_WHITE = (255, 250, 250)


def text_on_img(text="NULL", filename='output.png', text_size=120, image_w=200, image_h=200):
    "Draw a text on an Image, saves it"
    fnt = ImageFont.truetype('arial.ttf', text_size)
    # create image
    image = Image.new(mode="RGB", size=(200, 200), color="black")
    draw = ImageDraw.Draw(image)

    # get center of img to put text
    text_w, text_h = fnt.getsize(text)

    # draw text
    draw.text(((image_w-text_w)/2, (image_h-text_h)/2),
              text, font=fnt, fill=(255, 250, 250))
    # save file
    image.save(filename)


@click.group()
def cli():
    """Base cli for click"""


@cli.command(name='tax')
@click.argument('tax', default='0', type=str)
def commander_tax(tax):
    """Make the command tax image"""
    text_on_img(text=tax, filename='command_tax.png')


@cli.command(name='life')
@click.argument('life_count', default='40', type=str)
def life_counter(life_count):
    "Make the life counter image"
    text_on_img(text=life_count, filename='life_count.png')


if __name__ == "__main__":
    cli()
