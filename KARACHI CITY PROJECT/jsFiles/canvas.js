export class canvasRender {
    constructor(canvas) {
        this.canvas = canvas
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(40, this.canvas.offsetWidth / this.canvas.offsetHeight, 0.1 ,1000);
        this.orient = new THREE.Vector3(0,0,0);
        this.renderer = new THREE.WebGLRenderer({
            antialias:true,
            canvas: this.canvas
          });
    }
    setRenderer = () => {
        this.renderer.setSize(this.canvas.offsetWidth, this.canvas.offsetHeight);
        //Initilize empty Canvas
        this.renderer.render(this.scene, this.camera);
    }

    render = () => {
        this. renderer.render(this.scene, this.camera);
       
    }


}