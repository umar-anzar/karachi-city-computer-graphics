//By Izhan 048, Modifed by Umar 104
export class Movement {
    constructor(window,camera) {
        this.keyList = ["a","d","w","s","q","e","ArrowRight","ArrowLeft","ArrowUp","ArrowDown"];
        this.camera = camera;
        this.window = window;
        this.movingTimeout = -1;
        this.FPS = 120;
        this.myWorldYAxis = new THREE.Vector3(0, 1, 0);
        this.keySet = {};
        this.speed = 0.5;
        this.rotationSpeed = 0.05;
    }
//Object.keys(this.keySet)
    keyRelease = (e) => {
      if (this.keyList.includes(e.key)) {
        if (this.keySet[e.key] != undefined) {
          this.stopMoving(this.keySet[e.key]);
          delete this.keySet[e.key];
        }
      }
    }
    keyPress = (e) => {
      if (this.keyList.includes(e.key)) {
          if (this.keySet[e.key] == undefined) {
            this.keySet[e.key] = -1;
            const keysPressed = Object.keys(this.keySet);
            for (let index = 0; index < keysPressed.length; index++) {
              this.startMoving(keysPressed[index]);
            }
          }
        }
    }

    stopMoving = (movingTimeout) => {
        clearTimeout(movingTimeout);
        movingTimeout = -1;
    }

    startMoving = (key) => {
      
        if (this.keySet[key] === -1) {      
            this.cameraMove(key);
        }
    }

    cameraMove = (key) => {
        if (key == "a") {
          this.camera.translateX(-this.speed);
        }
        else if (key == "d") {
          this.camera.translateX(this.speed);
        }
        else if (key == "w") {
          this.camera.translateZ(-this.speed);
        }
        else if (key == "s") {
          this.camera.translateZ(this.speed);
        }
        else if (key == "q") {
          this.camera.translateY(this.speed);
        }
        else if (key == "e") {
          this.camera.translateY(-this.speed);
        }
        else if (key == "ArrowRight") {
          this.camera.rotateOnWorldAxis(this.myWorldYAxis,-this.rotationSpeed);
        }
        else if (key == "ArrowLeft") {
          this.camera.rotateOnWorldAxis(this.myWorldYAxis,this.rotationSpeed);
        }
        else if (key == "ArrowUp") {
          this.camera.rotateX(this.rotationSpeed);
        }
        else if (key == "ArrowDown") {
          this.camera.rotateX(-this.rotationSpeed);
        }
       this.keySet[key] = setTimeout(this.cameraMove,1000/this.FPS,key);
    }

}
