import { defineElement } from "../../utils/defineElement";

export const SHOW_FILTERS_EVENT = 'x-filters-drawer:open';

class FiltersDrawer extends HTMLElement {
  get _close() {
    return this.querySelector('[data-close]');
  }

  get _content() {
    return this.querySelector('[data-content]');
  }

  close = () => {
    this._content.classList.remove('fadeInRightBig');
    this._content.classList.add('fadeOutRightBig');
    this._content.addEventListener('animationend', this.afterClose, { once: true })
  }

  afterClose = () => {
    this._content.classList.remove('fadeOutRightBig');
    this.classList.remove('active');
  }

  open = () => {
    this._content.removeEventListener('animationend', this.afterClose);
    this.classList.add('active');
    this._content.classList.add('fadeInRightBig');
  }

  init() {
    document.addEventListener(SHOW_FILTERS_EVENT, this.open);
    this._close.addEventListener('click', this.close);
  }

  cleanup() {
    document.removeEventListener('x-filters-drawer:open', this.open);
    this._close.removeEventListener('click', this.close);
  }

  constructor() {
    super()

    this.addEventListener('htmx:beforeSwap', this.cleanup)
    this.addEventListener('htmx:afterSwap', this.init)
  }

  disconnectedCallback() {
    this.cleanup()
  }
}

defineElement('x-filters-drawer', FiltersDrawer);
