// Page behaviour: scroll reveals, tagline word reveal, draft/fixed demo toggle,
// install-command copy, mobile menu, and current-section nav state.
(() => {
  const root = document.documentElement;
  root.classList.add("js");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Sections rise into place once. Transform only, so text is readable at every scroll position.
  const revealIO = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("is-in"); revealIO.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll("[data-reveal]").forEach((el) => revealIO.observe(el));

  // Tagline: each word turns from the muted tone to full text as it crosses 60% of the viewport.
  const tagline = document.querySelector("[data-tagline]");
  if (tagline) {
    const text = tagline.textContent.trim();
    // Split on plain whitespace only: a no-break space (U+00A0) keeps "bản dịch." on one line.
    const words = text.split(/[ \t\r\n]+/).map((w) => `<span class="w" aria-hidden="true">${w}</span>`);
    tagline.innerHTML = `<span class="sr-only">${text}</span>${words.join(" ")}`;
    const spans = [...tagline.querySelectorAll(".w")];
    let ticking = false;
    // Words sharing a row activate left to right over the last 96px of scroll before the line.
    const paint = () => {
      const line = window.innerHeight * 0.6;
      const box = tagline.getBoundingClientRect();
      spans.forEach((s) => {
        const r = s.getBoundingClientRect();
        const along = (r.left - box.left) / Math.max(box.width, 1);
        s.classList.toggle("on", reduced || r.top + along * 96 < line);
      });
      ticking = false;
    };
    const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    paint();
  }

  // Graded draft demo: switch between the AI draft and the corrected copy.
  document.querySelectorAll("[data-demo]").forEach((demo) => {
    const buttons = demo.querySelectorAll("[data-show]");
    buttons.forEach((btn) => btn.addEventListener("click", () => {
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
      demo.querySelectorAll("[data-state]").forEach((p) => { p.hidden = p.dataset.state !== btn.dataset.show; });
    }));
  });

  // Copy the install command.
  document.querySelectorAll("[data-copy]").forEach((btn) => {
    const source = document.getElementById(btn.dataset.copy);
    const status = document.getElementById(btn.dataset.status);
    const label = btn.querySelector("[data-label]");
    const idleLabel = label.textContent;
    btn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(source.textContent.trim());
        status.textContent = "Đã chép lệnh cài đặt. Dán vào terminal để chạy.";
        status.className = "copy-status ok";
        label.textContent = "Đã chép";
        setTimeout(() => { label.textContent = idleLabel; }, 2000);
      } catch {
        status.textContent = "Trình duyệt chặn quyền chép. Hãy bôi đen lệnh và chép thủ công.";
        status.className = "copy-status err";
      }
    });
  });

  // Mobile menu: full height panel, Escape closes, focus returns to the toggle.
  const toggle = document.querySelector(".menu-toggle");
  const menu = document.getElementById("mobile-menu");
  const main = document.getElementById("main");
  const setMenu = (open) => {
    root.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Đóng menu" : "Mở menu");
    main.inert = open;
    document.querySelector(".footer").inert = open;
    if (open) menu.querySelector("a").focus(); else toggle.focus();
  };
  toggle.addEventListener("click", () => setMenu(!root.classList.contains("menu-open")));
  menu.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && root.classList.contains("menu-open")) setMenu(false);
  });

  // Mark the nav link of the section under a line at 40% of the viewport, in the desktop bar and the
  // mobile menu. Above the first linked section (the hero) nothing is marked.
  const links = [...document.querySelectorAll(".nav-links a, .mobile-menu a")].filter((a) => a.hash);
  const targets = new Map();
  links.forEach((a) => { const s = document.querySelector(a.hash); if (s) targets.set(s, a.hash); });
  // A section without its own link counts toward the one it belongs to (data-nav-for="id").
  document.querySelectorAll("[data-nav-for]").forEach((s) => targets.set(s, `#${s.dataset.navFor}`));
  let spyTicking = false;
  const spy = () => {
    spyTicking = false;
    const line = window.innerHeight * 0.4;
    let current = "";
    targets.forEach((hash, section) => {
      const r = section.getBoundingClientRect();
      if (r.top <= line && r.bottom > line) current = hash;
    });
    links.forEach((a) => {
      if (a.hash === current) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
    });
  };
  const onSpy = () => { if (!spyTicking) { spyTicking = true; requestAnimationFrame(spy); } };
  window.addEventListener("scroll", onSpy, { passive: true });
  window.addEventListener("resize", onSpy);
  spy();
})();
