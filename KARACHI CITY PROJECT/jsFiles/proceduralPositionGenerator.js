//Muhammad Umar Anzar B19102104
export function buildingPositionGenerator(planeW,planeH,topCorner,xOffset,yOffset,xTiles,yTiles) {

    let leftBorder = {
                  x: topCorner.x + xOffset , 
                  y: topCorner.y - yOffset
              };
    
    let singleTile = { W:planeW / xTiles, L: planeH / yTiles};
  
    let buildingTile = { W:singleTile.W - 2*xOffset, L: singleTile.L - 2*yOffset };
    
  
    let buildingDiv = 2;
    let maxBuildingSize = { W: buildingTile.W / buildingDiv , L: buildingTile.L / buildingDiv };
    
    
    let b_one, b_two;
  
  
    //position generator of buildings
    let positionArray = []
    for (let row = 0; row < yTiles; row++) {
      b_one = {x: leftBorder.x + maxBuildingSize.W / 2 , y: leftBorder.y - maxBuildingSize.L / 2 };
      b_one.y -= row*(buildingTile.L + 2*xOffset);
      b_two = {x: b_one.x ,y: b_one.y - maxBuildingSize.L};
      for (let col = 0; col < xTiles*2; col++) {
        if (col == 6 || col == 7 || col==8 || col==9){continue;}
        let pos1 = [b_one.x + col*maxBuildingSize.W, b_one.y];
        let pos2 = [b_two.x + col*maxBuildingSize.W, b_two.y];
        positionArray.push(pos1,pos2);
        if (col % 2 != 0) {
          b_one.x += 2*xOffset;
          b_two = {x: b_one.x ,y: b_one.y - maxBuildingSize.L};
        }
      }
    }
    return [positionArray,maxBuildingSize];
}


export function generateRandomSize(maxW,maxL,maxH) {
    let W = Math.floor(Math.random() * maxW) + 1;
    let L = Math.floor(Math.random() * maxL) + 1;
    let H = Math.floor(Math.random() * maxH) + 1;
    if (W<10) {
      W = 10;
    }
    if (L<20) {
      L = 20;
    }
    if (H<30) {
      H = 30;
    }
    return [W,L,H]
  }