//Canvas
var canvas = document.getElementById("myCanvas");

//Scene Perspective and Render
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(40, canvas.offsetWidth / canvas.offsetHeight, 0.1, 1000);

var renderer = new THREE.WebGLRenderer({ canvas: myCanvas });

renderer.setSize(canvas.offsetWidth, canvas.offsetHeight);
//Initilize empty Canvas
renderer.render(scene, camera);

camera.position.set(0, 10, 0);

camera.lookAt(0, 0, 0);

//Creating Cube
const geometry = new THREE.BoxGeometry( 1, 1, 1 );
const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
var cube = new THREE.Mesh( geometry, material );
var cube2 = new THREE.Mesh( geometry, material );
var cube3 = new THREE.Mesh( geometry, material );
scene.add( cube );
scene.add( cube2 );
scene.add( cube3 );

cube2.position.x = 3;
cube3.position.x = -3;

var radian = (angle) => angle*180/Math.PI;
//Rotation variable
var i = 0.001



//FPS
var last_time = 0;
var current_time = 0
var fps=60;
var delta_time = 1000 / fps;


//Set Fps function
var fps_tag = document.getElementById("fps");
var fps_label = document.getElementById("fpsLabel");

var BtnSetFps = () => {

    fps = Number(fps_tag.value);

    if (isNaN(fps)) {
        fps=60;
    }

    fps_label.innerHTML = "Fps: "+fps
    delta_time = 1000 / fps;
}
BtnSetFps();

var pp = 0.1
var aa = 0
//Variables update function
var update = () => {
    aa += pp
    // camera.position.x+=Math.sin(aa)*0.3;
    // camera.position.z+=Math.cos(aa)*0.3;
    // cube.rotation.x += radian(i);
    // cube.rotation.y += radian(i);
    // cube.rotation.z += radian(i);
    
};

var render = () => renderer.render(scene, camera);


//GAMELOOP
var GameLoop = () => {
    update();

    current_time = new Date().getTime();
    if ((current_time - last_time) >=  delta_time) {
        render();
        last_time = current_time;
    }

    requestAnimationFrame(GameLoop);
};

GameLoop();