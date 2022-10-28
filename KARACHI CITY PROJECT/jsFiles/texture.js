//By Izhan 048, Modifed by Umar 104
const sides = ["ft", "bk", "up", "dn", "rt", "lf"];
export function boxTexture (location,name) {
  let materialArray = [];
  for (let i = 0; i < 6; i++) {
    let texture =  new THREE.TextureLoader().load(location+name+sides[i]+".bmp");
    materialArray.push(new THREE.MeshBasicMaterial( {map : texture, wireframe : false} ));
    materialArray[i].side = THREE.BackSide;
  }
  return materialArray;
}

export function simpleTexture(location,name) {
  let texture =  new THREE.TextureLoader().load(location+name+".bmp");
  return new THREE.MeshBasicMaterial( {map : texture, wireframe : false} )
}


export function buildingTexture(location,name,name2) {
  let materialArray = [];
  for (let i = 0; i < 6; i++) {
    if (i == 4 || i == 5){
      let texture =  new THREE.TextureLoader().load(location+name2+".bmp");
      materialArray.push(new THREE.MeshBasicMaterial( {map : texture, wireframe : false} ));
      materialArray[i].side = THREE.DoubleSide;
      continue;
    }
    let texture =  new THREE.TextureLoader().load(location+name+".bmp");
    materialArray.push(new THREE.MeshBasicMaterial( {map : texture, wireframe : false} ));
    materialArray[i].side = THREE.DoubleSide;
  }
  return materialArray;
}