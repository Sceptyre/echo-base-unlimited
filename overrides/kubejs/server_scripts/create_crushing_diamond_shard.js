ServerEvents.recipes(event => {
    event.recipes.create.crushing(
        [Item.of('spelunkery:rough_diamond_shard').withChance(0.5)],
        'spelunkery:diamond_shard'
    )
})