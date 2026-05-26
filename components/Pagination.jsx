export function Pagination({ total, pageSize, current, onChange }) {
  const totalPages = Math.ceil(total / pageSize);
  const range = [];
  for (let i = Math.max(1, current - 2); i <= Math.min(totalPages, current + 2); i++) {
    range.push(i);
  }
  return (
    <nav>
      {current > 3 && <span>1 … </span>}
      {range.map(p => (
        <button key={p} onClick={() => onChange(p)} aria-current={p === current ? "page" : undefined}>
          {p}
        </button>
      ))}
      {current < totalPages - 2 && <span> … {totalPages}</span>}
    </nav>
  );
}
