class TypeWriter {
  constructor(sentence, speed) {
    this.sentence = sentence;
    this.speed = speed;
  }

  type(page) {
    for (let i = 0; i < this.sentence.length; i++) {
      setTimeout(
        (y) => {
          page.innerHTML += this.sentence[y];
        },
        i * this.speed,
        i
      );
    }
  }
}
