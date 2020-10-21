# generated by cabal-rpm-2.0.6
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name gi-gdk
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        3.0.23
Release:        2%{?dist}
Summary:        Gdk bindings

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-gi-cairo-prof
BuildRequires:  ghc-gi-gdkpixbuf-prof
BuildRequires:  ghc-gi-gio-prof
BuildRequires:  ghc-gi-glib-prof
BuildRequires:  ghc-gi-gobject-prof
BuildRequires:  ghc-gi-pango-prof
BuildRequires:  ghc-haskell-gi-prof
BuildRequires:  ghc-haskell-gi-base-prof
BuildRequires:  ghc-haskell-gi-overloading-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  pkgconfig(gdk-3.0)
# End cabal-rpm deps

%description
Bindings for Gdk, autogenerated by haskell-gi.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gdk-3.0)
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# with dynamic Setup get:
# libHSgi-gio-2.0.25.so: error: undefined reference to 'g_tls_certificate_new_from_pkcs11_uris'
%define ghc_static_setup 1
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
chmod a-x ChangeLog.md README.md
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jens Petersen <petersen@redhat.com> - 3.0.23-1
- update to 3.0.23

* Fri Feb 14 2020 Jens Petersen <petersen@redhat.com> - 3.0.22-1
- update to 3.0.22

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 3.0.16-5
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 3.0.16-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 3.0.16-1
- spec file generated by cabal-rpm-0.12.6
