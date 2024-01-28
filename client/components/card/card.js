import { defineElement } from "../../utils/defineElement";

class Card extends HTMLElement {
  isQtyOpen = false;

  get _qty() {
    return this.querySelector('[data-qty]');
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

  get _form() {
    return this.querySelector('[data-form]');
  }

  get _confirm() {
    return this.querySelector('[data-confirm]');
  }

  get _toggleQty() {
    return this.querySelector('[data-toggle-qty]');
  }

  get _toggleQtyIcon() {
    return this.querySelector('[data-toggle-qty-icon]');
  }

  open = () => {
    this.isQtyOpen = true;
    this._qty.classList.add('card-open-qty');
    this._toggleQtyIcon.classList.remove('icon-shopping-cart', 'text-white');
    this._toggleQtyIcon.classList.add('icon-x', 'text-red-400');
  }

  close = () => {
    this.isQtyOpen = false;
    this._input.value = 0;
    this._qty.classList.remove('card-open-qty');
    this._toggleQtyIcon.classList.remove('icon-x', 'text-red-400');
    this._toggleQtyIcon.classList.add('icon-shopping-cart', 'text-white');
  }

  constructor() {
    super();

    this._qty.addEventListener('click', (e) => {
      e.stopPropagation();
      e.preventDefault();
    });

    this._add.addEventListener('click', () => {
      const value = parseInt(this._input.value || 0, 10);
      this._input.value = value + 1;
    });

    this._minus.addEventListener('click', () => {
      const value = parseInt(this._input.value || 0, 10);

      if (value <= 0) {
        return;
      }

      this._input.value = value - 1;
    });

    this._toggleQty.addEventListener('click', () => {
      if (!this.isQtyOpen) {
        return this.open();
      }

      this.close();
    });

    this._confirm.addEventListener('click', () => {
      window.htmx.trigger(this._form, "x-submit");
      this.close();
    });
  }
}

defineElement('x-card', Card);
