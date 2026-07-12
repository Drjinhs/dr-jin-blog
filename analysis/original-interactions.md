# Source interaction analysis

The authorized preview exposed anchor navigation, a mobile menu, activity-category filters, external article links, and a contact form. The implementation covers these interactions:

- Fixed navigation gains a translucent background after scrolling.
- Anchor links scroll to matching semantic sections.
- Active desktop navigation updates as sections enter the reading area.
- Mobile navigation exposes `aria-expanded` and `aria-controls`, closes on selection and Escape, and preserves 44px touch targets.
- Content reveals as it enters the viewport through `IntersectionObserver`.
- All content remains visible without JavaScript and motion is removed for reduced-motion users.
- External destinations open in a new tab with `noopener noreferrer`; email links use `mailto:`.
