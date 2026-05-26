import { useRef, useEffect, useState } from "react";

export function LazyImage({ src, alt, ...props }) {
  const [loaded, setLoaded] = useState(false);
  const ref = useRef();

  useEffect(() => {
    const obs = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        ref.current.src = src;
        obs.disconnect();
      }
    });
    obs.observe(ref.current);
    return () => obs.disconnect();
  }, [src]);

  return <img ref={ref} alt={alt} onLoad={() => setLoaded(true)} data-loaded={loaded} {...props} />;
}
