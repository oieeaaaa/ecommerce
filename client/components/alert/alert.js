import { defineElement } from "../../utils/defineElement";

class Alert extends HTMLElement {
  get _close() {
    return this.querySelector('[data-close]');
  }

  close = () => {
    this.classList.add('hidden');
  }

  constructor() {
    super()

    this._close.addEventListener('click', this.close);
  }
}

defineElement('x-alert', Alert);
