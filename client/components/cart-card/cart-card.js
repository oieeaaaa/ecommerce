import { defineElement } from "../../utils/defineElement";

class CartCard extends HTMLElement {
  get _form() {
    return this.querySelector('[data-form]');
  }

  get _add() {
    return this.querySelector('[data-add]');
  }

  get _input() {
    return this.querySelector('[data-input]');
  }

  get _minus() {
    return this.querySelector('[data-minus]');
  }

  constructor() {
    super();

    this._add.addEventListener('click', () => {
      const value = parseInt(this._input.value || 0, 10);
      this._input.value = value + 1;

      window.htmx.trigger(this._form, 'cart_qty_updated');
    });

    this._minus.addEventListener('click', () => {
      const value = parseInt(this._input.value || 0, 10);

      if (value <= 0) {
        return;
      }

      this._input.value = value - 1;

      window.htmx.trigger(this._form, 'cart_qty_updated');
    });

    this._input.addEventListener('change', () => {
      window.htmx.trigger(this._form, 'cart_qty_updated');
    })
  }
}

defineElement('x-cart-card', CartCard);
