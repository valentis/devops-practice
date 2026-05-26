import { useEffect, useRef, useCallback } from "react";

export function useInfiniteScroll(onLoadMore, hasNextPage) {
  const observerRef = useRef(null);
  const sentinelRef = useRef(null);

  const handleObserve = useCallback((entries) => {
    if (entries[0].isIntersecting && hasNextPage) {
      onLoadMore();
    }
  }, [onLoadMore, hasNextPage]);

  useEffect(() => {
    if (observerRef.current) observerRef.current.disconnect();
    observerRef.current = new IntersectionObserver(handleObserve, {
      rootMargin: "200px",
    });
    if (sentinelRef.current) {
      observerRef.current.observe(sentinelRef.current);
    }
    return () => observerRef.current?.disconnect();
  }, [handleObserve]);

  return sentinelRef;
}
