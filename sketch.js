let cars = [5];
let frog1;
let carsNum = 5;
let sceneNum = 0;
let frogLives = 7;
let frog;
let carImg = [];

let hero;
let coins = [];

let points = 0;

//preloading
function preload() {
  frog = loadImage("assets/frog.png");

  for (let i = 0; i < 5; i++) {
    carImg[i] = loadImage("assets/car" + i + ".png");
  }
}

//setup
function setup() {
  createCanvas(600, 400);

  for (let i = 0; i < carsNum; i++) {
    cars[i] = new Car(
      random(width),
      random(height - 150),
      color(random(255), random(255), random(255))
    );
  }
  
   for (let i = 0; i < 15; i++) {
    coins[i] = new Reward();
  }

  frog1 = new Frog();
}

function draw() {
  background(220);

  for (let i = 0; i < carsNum; i++) {
    cars[i].body(i);
    cars[i].move();
    cars[i].checkCollision();
  }
  
   for (let i = 0; i < coins.length; i++) {
    coins[i].display();
    coins[i].move();
    coins[i].checkCollision();
    
  }

  frog1.body();
  frog1.move();
  frog1.home();

  currentFrogLives();
}

function currentFrogLives() {
  for (let i = 0; i < frogLives; i++) {
    image(frog, i * 30, height - 20, frog.width * 0.7, frog.height * 0.7);
    
  }
}

//classes
class Frog {
  constructor() {
    this.x = width / 2;
    this.y = height - 50;
    this.w = 30;
    this.h = 30;
    this.c = color(0, 255, 0);
  }

  body() {
    imageMode(CENTER);
    frog.resize(50, 50);

    image(frog, this.x, this.y, frog.width * 1.2, frog.height * 1.2);
  }

  move() {
    if (keyIsDown(38)) {
      this.y -= 3;
    }
    if (keyIsDown(40)) {
      this.y += 3;
    }
    if (keyIsDown(39)) {
      this.x = this.x + 3;
    }
    if (keyIsDown(37)) {
      this.x = this.x - 3;
    }
  }

  
  home() {
    if (this.y < 0) {
      sceneNum++;
      this.y = height - 50;
    }

    if (sceneNum > 2) {
      sceneNum = 0;
    }
  }
  
}

class Car {
  constructor(x, y, c) {
    this.x = x;
    this.y = y;
    this.w = 50;
    this.h = 35;
    this.c = c;
  }

  body(index) {
    imageMode(CORNER);

    image(
      carImg[index],
      this.x - 20,
      this.y - 28,
      carImg[index].width * 0.28,
      carImg[index].height * 0.28
    );
  }

  move() {
    this.x++;

    if (this.x > width) {
      this.x = 0;
    }
  }

  //checking
  checkCollision() {
    if (
      frog1.x + frog1.w / 2 > this.x &&
      frog1.x < this.x + this.w &&
      frog1.y + frog1.h / 2 > this.y &&
      frog1.y < this.y + this.h
    ) {
      console.log("hit!");
      frog1.y = height - 50;
      frogLives--;
    }
  }
}

class Reward {
  constructor() {
    this.x = random(50, width - 50);
    this.y = random(20, height - 20);
    this.size = 20;
    this.color = "yellow";
  }
  display() {
    fill(this.color);
    ellipse(this.x, this.y, this.size, this.size);
  }
  
  move() {
    this.x++;

    if (this.x > width) {
      this.x = 0;
    }
  }
  
  checkCollision(index) {
    if (
      frog1.x + frog1.w / 2 > this.x &&
      frog1.x - frog1.w < this.x  &&
      frog1.y + frog1.h / 2 > this.y &&
      frog1.y - frog1.h< this.y
    ) {
      console.log("picked!");
      points ++
      this.x = random(50, width - 50);
      this.y = random(20, height - 20);
      
      console.log(points)
      
      
    }
  }

}




