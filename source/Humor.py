import math, string, random

class Humor():

    alphanums = string.ascii_uppercase + string.digits
    popularPlatforms = ["Fortnite", "Roblox", "Minecraft", "Among Us", "Microsoft Store", "Twitter Blue", "Discord Nitro"]

    @staticmethod
    # Creating a function that generates a fake giftcard
    def giftcardGenerator(k: int = 4) -> str:
        giftcard = [''.join(random.choices(Humor.alphanums, k=k)) for _ in range(4)]
        return '-'.join(giftcard)
    
    @staticmethod
    # Creating a function that formats time (from seconds to minutes, hours, etc.)
    def formatTime(time: int) -> str:
        # We first need to check if time is shorter than 60 seconds (1 minute)
        if time < 60:
            return f"{time} seconds"
        # If the check failed, we will try again this time checking if time is shorter than 3600 seconds (1 hour)
        if time < 3600:
            return f"{math.floor(time/60)} minutes and {time%60} seconds"
        # Both checks failed, now we know that there's over 1 hour
        return f"{math.floor(time/3600)} hours, {math.floor(time/60)%60} minutes and {time%60} seconds"