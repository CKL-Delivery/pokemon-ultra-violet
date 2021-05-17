// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`1000100002020e0e0505090404040c0d0d0d02020202010e0e05070404040b0d0d02020202020d0d0e0e070404040b0d0d0d020101020d0d0505070404040b0d0d0d0201010201050808070404040b0d0d010201010202030808070404040b0d0d0d0201010103030808070404040b0d0d0d0101010101030808070404040b0d0d010101010103050808070404040b0d0d0d0101010103050808070404040b0d0d0d0101010201030808070404040b0d0d010101010205050808070404040b0e0e0e0101010205050808070404040b0e0e0e0101010201050808070404040b0e0e010101010505050808070404040b0e0e0e0101010201050808060404040a0e0e010101`, img`
2 2 2 2 . . . . . . . . . . 2 2 
2 2 2 2 2 . . . . . . . . 2 2 2 
2 2 . . 2 2 . . . . . . . . 2 2 
2 2 . . . . . . . . . . . . 2 2 
2 2 2 . . . . . . . . . . 2 2 2 
2 2 2 2 . . . . . . . . . . 2 2 
2 2 2 2 . . . . . . . . . . 2 2 
2 2 2 2 . . . . . . . . . 2 2 2 
2 2 2 . . . . . . . . . . . 2 2 
2 2 2 . . . . . . . . . . . 2 2 
2 2 2 2 . . . . . . . . . 2 2 2 
2 2 . . . . . . . . . 2 2 2 2 2 
2 2 . . . . . . . . . 2 2 2 2 2 
2 2 2 . . . . . . . . 2 2 2 2 2 
2 . . . . . . . . . . 2 2 2 2 2 
2 2 2 . . . . . . . . 2 2 2 2 2 
`, [myTiles.transparency16,sprites.builtin.forestTiles16,sprites.builtin.forestTiles4,sprites.builtin.forestTiles8,sprites.castle.tilePath5,sprites.swamp.swampTile1,sprites.castle.tilePath7,sprites.castle.tilePath4,sprites.castle.tileGrass2,sprites.castle.tilePath1,sprites.castle.tilePath9,sprites.castle.tilePath6,sprites.castle.tilePath3,sprites.swamp.swampTile2,sprites.builtin.forestTiles27], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
