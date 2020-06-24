# generated by cabal-rpm-2.0.3
# https://fedoraproject.org/wiki/Packaging:Haskell

Name:           bustle
Version:        0.7.5
Release:        3%{?dist}
Summary:        Draw sequence diagrams of D-Bus traffic

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
# taken from ghc-hgettext
Patch0:         bustle-hgettext-Cabal24.patch
Patch1:         https://gitlab.freedesktop.org/bustle/bustle/commit/ee4b81cbc232d47ba9940f1987777b17452e71ff.patch

Requires:       gnome-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  help2man
# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-static
BuildRequires:  ghc-bytestring-static
BuildRequires:  ghc-cairo-static
BuildRequires:  ghc-containers-static
BuildRequires:  ghc-dbus-static
BuildRequires:  ghc-directory-static
BuildRequires:  ghc-filepath-static
BuildRequires:  ghc-gio-static
BuildRequires:  ghc-glib-static
BuildRequires:  ghc-gtk3-static
BuildRequires:  ghc-hgettext-static
BuildRequires:  ghc-mtl-static
BuildRequires:  ghc-pango-static
BuildRequires:  ghc-pcap-static
BuildRequires:  ghc-process-static
BuildRequires:  ghc-setlocale-static
BuildRequires:  ghc-text-static
BuildRequires:  ghc-time-static
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
# End cabal-rpm deps
ExcludeArch:    ppc64le

%description
Bustle records and draws sequence diagrams of D-Bus activity, showing signal
emissions, method calls and their corresponding returns, with timestamps for
each individual event and the duration of each method call. This can help you
check for unwanted D-Bus traffic, and pinpoint why your D-Bus-based application
isn't performing as well as you like. It also provides statistics like signal
frequencies and average method call times.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} INSTALL="install -p" install
#%%find_lang %%{name}

rm %{buildroot}%{_datadir}/%{name}-%{version}/LICENSE


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.freedesktop.Bustle.desktop


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CONTRIBUTING.md NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
# End cabal-rpm files
%{_bindir}/%{name}-pcap
%{_datadir}/appdata/org.freedesktop.Bustle.appdata.xml
%{_datadir}/applications/org.freedesktop.Bustle.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/%{name}-pcap.1*


%changelog
* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 0.7.5-3
- refresh to cabal-rpm-2.0.2
- re-enable hgettext

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  8 2019 Jens Petersen <petersen@redhat.com> - 0.7.5-1
- update to 0.7.5
- exclude ppc64le because of #1737587

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.7.4-1
- update to 0.7.4
- disable redundant hgettext

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Jens Petersen <petersen@redhat.com> - 0.7.1-2
- rebuild for static executable

* Sun Jul 22 2018 Jens Petersen <petersen@redhat.com> - 0.7.1-1
- update to 0.7.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 0.6.2-1
- update to 0.6.2

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-7
- Remove obsolete scriptlets

* Mon Aug 14 2017 Jens Petersen <petersen@redhat.com> - 0.5.4-6
- reenable i686 (#1427000)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Jens Petersen <petersen@redhat.com> - 0.5.4-3
- refresh to cabal-rpm-0.11.1
- exclude i686 due to missing deps (gcc7 __float128)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Jens Petersen <petersen@redhat.com> - 0.5.4-1
- update to 0.5.4

* Mon Mar  7 2016 Jens Petersen <petersen@redhat.com> - 0.4.8-7
- rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 22 2015 Jens Petersen <petersen@redhat.com> - 0.4.8-5
- rebuild

* Fri Jul  3 2015 Philip Withnall <philip@tecnocode.co.uk> - 0.4.8-4
- Rebuilt for ghc-setlocale 1.0.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Jens Petersen <petersen@redhat.com> - 0.4.8-2
- rebuild

* Thu Apr  2 2015 Jens Petersen <petersen@redhat.com> - 0.4.8-1
- update to 0.4.8

* Sat Feb 14 2015 Jens Petersen <petersen@redhat.com> - 0.4.7-6
- patch from git to build with pango/glib 0.13

* Fri Dec 12 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.4.7-5
- Rebuilt for libHSbase changes

* Sun Sep 21 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.4.7-4
- Rebuilt for ghc-setlocale 1.0.0.1

* Mon Sep  8 2014 Jens Petersen <petersen@redhat.com> - 0.4.7-3
- rebuild (for libHSdbus bump)

* Mon Sep 1 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.4.7-2
- Rebuilt for ghc-setlocale 1.0.0

* Tue Aug 12 2014 Philip Withnall <philip@tecnocode.co.uk> - 0.4.7-1
- spec file generated by cabal-rpm-0.8.11
