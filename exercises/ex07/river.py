"""File to define River class."""

__author__ = "730566374"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages for fish."""
        fish_survive: list[Fish] = []
        bear_survive: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                fish_survive.append(fish)
                # add living fish
        for bear in self.bears:
            if bear.age <= 5:
                bear_survive.append(bear)
                # add living bear
        self.bears = bear_survive
        self.fish = fish_survive
        return None

    def bears_eating(self):
        """How many bears are eatin."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
            else:
                bear.hunger_score = -1
        return None

    def check_hunger(self):
        """Hunger for them bears."""
        bear_surv: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bear_surv.append(bear)
                # add living bear
        self.bears = bear_surv
        return None

    def repopulate_fish(self):
        """More fish."""
        for _ in range(0, len(self.fish) // 2):
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """More bears."""
        for _ in range(0, len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """How many fish and bears in the river?"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls one_river_day seven times."""
        for _ in range(0, 7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove 'amount' of fish from front of fish line at index 0."""
        for _ in range(min(amount, len(self.fish))):
            self.fish.pop(0)
