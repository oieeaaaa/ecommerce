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
        this.isQtyOpen = true;
        this._qty.classList.add('card-open-qty');
        this._toggleQtyIcon.classList.remove('icon-shopping-cart');
        this._toggleQtyIcon.classList.add('icon-x');
        return;
      }

      this.isQtyOpen = false;
      this._input.value = 0;
      this._qty.classList.remove('card-open-qty');
      this._toggleQtyIcon.classList.remove('icon-x');
      this._toggleQtyIcon.classList.add('icon-shopping-cart');
    });

    // TODO:
    // - Test this with multiple cards on the page
    this._confirm.addEventListener('click', () => {
      window.htmx.trigger(this._form, "x-submit");
    });
  }
}

defineElement('x-card', Card);
