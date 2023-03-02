from pydub import AudioSegment

def split_mp3(input_file, output_prefix, start1, end1, start2, end2):
    sound = AudioSegment.from_mp3(input_file)

    # Split the sound into three segments
    segment1 = sound[start1*1000:end1*1000]
    segment2 = sound[start2*1000:end2*1000]
    segment3 = sound[end2*1000:]

    # Save each segment to a separate file
    segment1.export(f"{output_prefix}-part1.mp3", format="mp3")
    segment2.export(f"{output_prefix}-part2.mp3", format="mp3")
    segment3.export(f"{output_prefix}-part3.mp3", format="mp3")

# Example usage:
split_mp3('St.mp3', 'Sp', 0, 60, 90, 120)
