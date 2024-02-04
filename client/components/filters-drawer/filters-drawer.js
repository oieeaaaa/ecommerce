import { defineElement } from "../../utils/defineElement";

export const SHOW_FILTERS_EVENT = 'x-filters-drawer:open';

class FiltersDrawer extends HTMLElement {
  get _close() {
    return this.querySelector('[data-close]');
  }

  close = () => {
    this.classList.add('hidden');
  }

  open = () => {
    console.log('open');
    this.classList.remove('hidden');
  }

  constructor() {
    super()

    document.addEventListener(SHOW_FILTERS_EVENT, this.open);
    this._close.addEventListener('click', this.close);
  }

  disconnectedCallback() {
    document.removeEventListener('x-filters-drawer:open', this.open);
    this._close.removeEventListener('click', this.close);
  }
}

defineElement('x-filters-drawer', FiltersDrawer);
