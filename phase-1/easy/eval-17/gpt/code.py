from typing import List


def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many
    beats each note lasts.

    Legend:
        'o'  – whole note, lasts four beats
        'o|' – half note, lasts two beats
        '.|' – quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    # Mapping from note symbols to their beat lengths
    note_to_beats = {"o": 4, "o|": 2, ".|": 1}

    # Split the input by whitespace and map each token to its beat value
    beats: List[int] = []
    for token in music_string.split():
        if token not in note_to_beats:
            raise ValueError(f"Unknown note symbol encountered: {token}")
        beats.append(note_to_beats[token])

    return beats
