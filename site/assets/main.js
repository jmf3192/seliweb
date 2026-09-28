document.querySelectorAll('[data-year]').forEach(node => { node.textContent = new Date().getFullYear(); });

const dialog = document.querySelector('.lightbox');
const images = [...document.querySelectorAll('[data-lightbox]')];
let activeIndex = 0;
let returnFocus = null;
function showImage(index) {
  activeIndex = (index + images.length) % images.length;
  const link = images[activeIndex];
  const image = dialog.querySelector('.lightbox-image');
  image.src = link.href;
  image.alt = link.querySelector('img').alt;
  dialog.querySelector('.lightbox-caption').textContent = link.dataset.caption;
  dialog.querySelector('.lightbox-count').textContent = `${activeIndex + 1} / ${images.length}`;
}
images.forEach((link, index) => link.addEventListener('click', event => {
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || typeof dialog.showModal !== 'function') return;
  event.preventDefault();
  returnFocus = link;
  showImage(index);
  dialog.showModal();
}));
dialog.querySelector('.lightbox-close').addEventListener('click', () => dialog.close());
dialog.querySelector('.lightbox-prev').addEventListener('click', () => showImage(activeIndex - 1));
dialog.querySelector('.lightbox-next').addEventListener('click', () => showImage(activeIndex + 1));
dialog.addEventListener('keydown', event => {
  if (event.key === 'ArrowLeft') { event.preventDefault(); showImage(activeIndex - 1); }
  if (event.key === 'ArrowRight') { event.preventDefault(); showImage(activeIndex + 1); }
});
dialog.addEventListener('close', () => returnFocus?.focus());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
document.querySelectorAll('video').forEach(video => video.addEventListener('play', () => {
  document.querySelectorAll('video').forEach(other => { if (other !== video) other.pause(); });
}));
