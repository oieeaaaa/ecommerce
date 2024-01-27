export const defineElement = (name, element) => {
  if (customElements.get(name)) {
    return;
  }

  customElements.define(name, element);
}
