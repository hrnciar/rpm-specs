%global forgeurl https://gitlab.com/lanodan/badWolf

Name:           badwolf
Version:        1.0.3
Release:        1%{?dist}
Summary:        Web Browser which aims at security and privacy over usability

%global tag v%{version}
%forgemeta

License:        BSD
URL:            https://hacktivis.me/projects/badwolf
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

BuildRequires:  webkit2gtk3-devel

Requires:       hicolor-icon-theme

%description
BadWolf is a minimalist and privacy-oriented WebKitGTK+ browser.

- Privacy-oriented:
No browser-level tracking, multiple ephemeral isolated sessions per new
unrelated tabs, JavaScript off by default.

- Minimalist:
Small codebase (~1 500 LoC), reuses existing components when available or makes
it available.

- Customizable:
WebKitGTK native extensions, Interface customizable through CSS.

- Powerful & Usable:
Stable User-Interface; The common shortcuts are available (and documented), no
vi-modal edition or single-key shortcuts are used.

- No annoyances:
Dialogs are only used when required (save file, print, …), javascript popups
open in a background tab.


%prep
%autosetup -n badWolf-%{tag}


%build
%set_build_flags
%make_build all


%install
%make_install PREFIX=%{_prefix}

rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%find_lang Badwolf


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files -f Badwolf.lang
%license COPYING
%doc README.md KnowledgeBase.md interface.txt
%{_bindir}/badwolf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/*
%dir %{_datadir}/%{name}/locale/*/LC_MESSAGES
%{_datadir}/%{name}/interface.css
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Sep  4 2020 Lyes Saadi <fedora@lyes.eu> - 1.0.3-1
- Update to 1.0.3.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  9 2020 Lyes Saadi <fedora@lyes.eu> - 1.0.2-1
- Update to 1.0.2.

* Sat Jul  4 2020 Lyes Saadi <fedora@lyes.eu> - 1.0.0-2
- RHBZ#1853858.

* Sat Jul  4 2020 Lyes Saadi <fedora@lyes.eu> - 1.0.0-1
- Initial package.
