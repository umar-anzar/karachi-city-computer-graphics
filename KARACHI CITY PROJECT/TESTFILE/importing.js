 // gltf, fbx and obj are supported by threejs

 var scene, camera, renderer, intensity, hlight;
 scene = new THREE.Scene();
 camera = new THREE.PerspectiveCamera(40, window.innerWidth/window.innerHeight ,1 ,5000);
 camera.position.set(0,0,5);
 scene.background = new THREE.Color(0xf7f7f7);
 
intensity = 4

hlight = new THREE.AmbientLight(0x404040, intensity);
 scene.add(hlight)
 renderer = new THREE.WebGLRenderer({
    antialias:true,
    canvas:document.querySelector(".three")
  });
renderer.setSize(window.innerWidth,window.innerHeight);
document.body.appendChild(renderer.domElement);
 
let loader = new THREE.GLTFLoader();
loader.load('/vite-project/material/assets/scene.gltf', function(gltf){
	scene.add(gltf.scene);
	const car = gltf.scene.children[0];
	car.scale.set(0.1, 0.1, 0.1);
	car.position.set(0,0,0);
	renderer.render(scene,camera);
})


 function animate() {
    renderer.render(scene,camera);
    requestAnimationFrame(animate);
  }
  
 // animate();
  