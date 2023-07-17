function f(y, x) {
  return y + 7;
}

const x0 = 0;
let y0 = 2;
const a = 0;
const b = 10;
const Num = 100;
const h = (b - a) / Num;

const x_points = Array.from({ length: Num }, (_, i) => a + i * h);
const y_points = [];

for (const x of x_points) {
  y_points.push(y0);
  const k1 = h * f(y0, x);
  const k2 = h * f(y0 + 0.5 * k1, x + 0.5 * h);
  const k3 = h * f(y0 + 0.5 * k2, x + 0.5 * h);
  const k4 = h * f(y0 + k3, x + h);
  y0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
}

// Plotar gráfico usando uma biblioteca de plotagem como Chart.js ou D3.js
// Por exemplo, usando Chart.js:
const ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: x_points,
    datasets: [
      {
        label: 'função dy/dx = y + 7',
        data: y_points,
        backgroundColor: 'transparent',
        borderColor: '#FF4500',
        borderWidth: 1.5,
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: 'Gráfico da função',
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'x',
        },
      },
      y: {
        title: {
          display: true,
          text: 'y',
        },
      },
    },
  },
});
