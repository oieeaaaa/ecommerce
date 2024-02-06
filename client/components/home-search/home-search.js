import { defineElement } from "../../utils/defineElement";
import { SHOW_FILTERS_EVENT } from "../filters-drawer/filters-drawer.js";

class HomeSearch extends HTMLElement {
  get _filter() {
    return this.querySelector('[data-filter]');
  }

  filterShowEvent = new Event(SHOW_FILTERS_EVENT);

  showFilters = () => {
    console.log('showFilters', SHOW_FILTERS_EVENT);

    document.dispatchEvent(this.filterShowEvent);
  }

  constructor() {
    super()

    console.log('HomeSearch');

    this._filter.addEventListener('click', this.showFilters);
  }
}

defineElement('x-home-search', HomeSearch);
