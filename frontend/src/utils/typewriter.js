export const typeText = (text, cb, speed = 15) => {
  let i = 0;
  const interval = setInterval(() => {
    cb(text.slice(0, i));
    i++;
    if (i > text.length) clearInterval(interval);
  }, speed);
};
