Name: swayidle
Version: 1.6
Release: 2%{?dist}
Summary: An idle daemon for wayland compositors

License: MIT and LGPLv2+
URL: https://github.com/swaywm/swayidle
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: fix-control-reaches-end.patch

BuildRequires: meson >= 0.48.0
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols) >= 1.14
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: scdoc

%description
swayidle is an idle management daemon for Wayland compositors.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/fish/vendor_completions.d/swayidle.fish
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_mandir}/man1/%{name}.1.gz

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Jack Hildebrandt <jack@jackhil.de> - 1.6-1
- Update to 1.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Jack Hildebrandt <jack@jackhil.de> - 1.5-1
- Update to 1.5. (1.4 is the same)

* Sun May 05 2019 Jack Hildebrandt <jack@jackhil.de> - 1.3-1
- Update to 1.3

* Sun Apr 07 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-5
- Add patch for "control reaches end of non-void function" error

* Wed Mar 20 2019 Jack Hildebradnt <jack@jackhil.de> - 1.2-4
- Fix license tag

* Mon Mar 18 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-3
- Flip changelog

* Fri Mar 15 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-2
- Fix directory ownership
- Clean up spec file

* Fri Mar 15 2019 Jack Hildebrandt <jack@jackhil.de> - 1.2-1
- Initial packaging

