import { useEffect, useRef } from "react";

export function Modal({ id, title, onClose, children }) {
  const modalRef = useRef();

  useEffect(() => {
    const handleKey = (e) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", handleKey);
    modalRef.current?.focus();
    return () => document.removeEventListener("keydown", handleKey);
  }, [onClose]);

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby={`${id}-title`}
      ref={modalRef}
      tabIndex={-1}
    >
      <h2 id={`${id}-title`}>{title}</h2>
      {children}
      <button onClick={onClose} aria-label="Close dialog">✕</button>
    </div>
  );
}
