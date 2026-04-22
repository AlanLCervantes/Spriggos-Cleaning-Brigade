init python:

    def street_items_total():
        return sum(store.street_items.values())

    def can_normal_end():
        return (
            street_items_total() >= 2 and
            store.fishes_n >= 4 and
            store.flowers_n >= 4 and
            store.trees_n >= 4
        )

    def can_secret_end():
        return (
            all(v >= 1 for v in store.street_items.values()) and
            store.fishes_n >= 8 and
            store.flowers_n >= 8 and
            store.trees_n >= 8
        )