import { canvasRender } from "./canvas.js";
import {Movement} from "./cameraMoving.js";
import {boxTexture,simpleTexture,buildingTexture} from './texture.js';
import {buildingPositionGenerator,generateRandomSize} from './proceduralPositionGenerator.js';

function toRadian(degree){
  return degree * Math.PI/180;
}


const canvas = document.getElementById("myCanvas");

const CVOBJ = new canvasRender(canvas)
CVOBJ.setRenderer();


const axesHelper = new THREE.AxesHelper( 5 );
CVOBJ.scene.add( axesHelper );


//Camera Position and Movement----------------------------------------------------- 
CVOBJ.camera.position.set(0,100,200);
CVOBJ.camera.rotateX(toRadian(-20));
var movement = new Movement(window,CVOBJ.camera);
window.onkeyup = function (e) {
   movement.keyRelease(e);
  }
  window.onkeydown = function (e) {
    movement.keyPress(e);
  }


// TEXTURE------------------------------------------------------------------
let skyboxTextureMaterial = boxTexture("material/skybox/","skybox_");
let roadTexture = simpleTexture("material/road/","road1");
var texture = []
for (let index = 0; index < 5; index++) {
  //texture.push(new THREE.TextureLoader().load("material\\buildingTex\\buildingtex"+ (index+1) +".bmp"));
  texture.push(buildingTexture("material\\buildingTex\\","buildingtex"+(index+1),"topBottom"));
}



var skyboxGeo = new THREE.BoxGeometry(400, 400, 400);
var skybox = new THREE.Mesh(skyboxGeo, skyboxTextureMaterial);
  
CVOBJ.scene.add(skybox);

// Plane ---------------------------------------------------------------------
let p_widht = 320;
let p_length = 180;
let xTiles = 8;
let yTiles = 3;
let p_topCornerVertex = {
                          x:-p_widht/2,
                          y:p_length/2
                      }; 
const planeGeometry = new THREE.PlaneGeometry(p_widht, p_length, xTiles, yTiles);

const planeMaterial = new THREE.MeshBasicMaterial({
    color: 0x808080, 
    side: THREE.DoubleSide,
    wireframe: false
} );
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
CVOBJ.scene.add(plane);

plane.rotation.set(toRadian(-90), 0, 0) //plane rotatin set
plane.position.set(0, -5, 0)

//Road-------------------------------------------------------------------------
let road_offsetX = 5
let road_offsetY = 5



//Building Position Generator--------------------------------------------------
let arrayAndSize = buildingPositionGenerator(p_widht,p_length,p_topCornerVertex,road_offsetX,road_offsetY,xTiles,yTiles);
let positionArray = arrayAndSize[0];
let maxBuildingSize = arrayAndSize[1];


//Creating Building with position Array
for (let index = 0; index < positionArray.length; index++) {

  const coor = positionArray[index];

  let size = generateRandomSize(maxBuildingSize.W,maxBuildingSize.L,70);
  const geometry = new THREE.BoxGeometry( size[0]-0.1, size[1]-0.1, size[2] );

  let randomTextureIndex = Math.abs(parseInt(Math.random()*texture.length-1))

  var cube = new THREE.Mesh( geometry, texture[randomTextureIndex]);

  cube.position.set(coor[0], coor[1], (cube.position.z+cube.geometry.parameters.depth/2)+0.1);

  plane.add(cube);
}


//GLTFLoader For 3D Object Loading--------------------------------------------------------------------IZHAN 048
let loader = new THREE.GLTFLoader();
loader.load('Assets/wall/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Dewar = gltf.scene.children[0];
	Dewar.scale.set(0.1, 0.1, 0.1);
  Dewar.rotateX(toRadian(-90));
	Dewar.position.set(50,1-p_length/2, 8);
  plane.add(gltf.scene);
  
});

loader.load('Assets/wall/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Dewar = gltf.scene.children[0];
	Dewar.scale.set(0.1, 0.1, 0.1);
  Dewar.rotateX(toRadian(-90));
	Dewar.position.set(-50,1-p_length/2, 8);
  plane.add(gltf.scene);
  
});


loader.load('Assets/rickshaw/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Rickshaw = gltf.scene.children[0];
	Rickshaw.scale.set(0.05, 0.05, 0.05);
  Rickshaw.rotateX(toRadian(90));
  Rickshaw.rotateZ(toRadian(180));
	Rickshaw.position.set(-40,30-p_length/2, 0);
  plane.add(gltf.scene);
  
})

loader.load('Assets/rickshaw/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Rickshaw = gltf.scene.children[0];
	Rickshaw.scale.set(0.05, 0.05, 0.05);
  Rickshaw.rotateX(toRadian(90));
  Rickshaw.rotateZ(toRadian(90));
	Rickshaw.position.set(0,60-p_length/2, 0);
  plane.add(gltf.scene);
  
})


loader.load('Assets/rickshaw/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Rickshaw = gltf.scene.children[0];
	Rickshaw.scale.set(0.05, 0.05, 0.05);
  Rickshaw.rotateX(toRadian(90));
  Rickshaw.rotateZ(toRadian(90));
	Rickshaw.position.set(60,120-p_length/2, 0);
  plane.add(gltf.scene);
  
})

loader.load('Assets/mazar/scene.glb', function(gltf){
	plane.add(gltf.scene);
	const Mazar = gltf.scene.children[0];
	Mazar.scale.set(0.05, 0.05, 0.05);
  Mazar.rotateX(toRadian(90));
  // Mazar.rotateZ(toRadian(90));
	Mazar.position.set(-60,0, 8);
  plane.add(gltf.scene);
  
})




let intensity = 4
let hlight = new THREE.AmbientLight(0x404040, intensity);
CVOBJ.scene.add(hlight)













var camera2 = new THREE.PerspectiveCamera(40, CVOBJ.canvas.offsetWidth / CVOBJ.canvas.offsetHeight, 0.1 ,1000);
camera2.lookAt(0,-1,0);
camera2.position.set(0,300,0);




//FPS
var last_time = 0;
var current_time = 0
var FPS = 30;
var delta_time = 1000 / FPS;





//Variables update function
var update = () => {

    
};

var render = () => CVOBJ.render();


//GAMELOOP
var GameLoop = () => {
    update();
    
    current_time = new Date().getTime();
    if ((current_time - last_time ) >=  delta_time) {
        
      CVOBJ.renderer.setViewport(0,0,CVOBJ.canvas.offsetWidth,CVOBJ.canvas.offsetHeight);
      CVOBJ.renderer.setScissor(0,0,CVOBJ.canvas.offsetWidth,CVOBJ.canvas.offsetHeight);
      CVOBJ.renderer.setScissorTest(false);
      CVOBJ.renderer.render(CVOBJ.scene,CVOBJ.camera);
      CVOBJ.renderer.setViewport(0,0,CVOBJ.canvas.offsetWidth/4,CVOBJ.canvas.offsetHeight/4);
      CVOBJ.renderer.setScissor(0,0,CVOBJ.canvas.offsetWidth/4,CVOBJ.canvas.offsetHeight/4);
      CVOBJ.renderer.setScissorTest(true);
      CVOBJ.renderer.render(CVOBJ.scene,camera2);




        last_time = current_time;
    }

    requestAnimationFrame(GameLoop);
};

GameLoop();