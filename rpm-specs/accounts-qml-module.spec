
Name:    accounts-qml-module
Summary: QML bindings for libaccounts-qt + libsignon-qt
Version: 0.7
Release: 1%{?dist} 

License: LGPLv2 
URL:     https://gitlab.com/accounts-sso/accounts-qml-module
Source:  https://gitlab.com/accounts-sso/%{name}/-/archive/VERSION_%{version}/%{name}-VERSION_%{version}.tar.bz2

## upstream patches
# PATCH-FIX-UPSTREAM
Patch1:  Fix-compilation-with-Qt-5.13.patch
# PATCH-FIX-UPSTREAM
Patch2:  Build-add-qmltypes-file-to-repository.patch

BuildRequires: qt5-doctools
BuildRequires: cmake(AccountsQt5)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(SignOnQt5)

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package doc
Summary: Documentation for %{name} 
BuildArch: noarch
%description doc
This package contains the developer documentation for accounts-qml-module.


%prep
%autosetup -n %{name}-VERSION_%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} \
  CONFIG+=release \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  ..
popd

%make_build -C %{_target_platform}


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

## unpackaged files
# remove tests
rm %{buildroot}%{_bindir}/tst_plugin
# avoid rpmlint warning
rm -fv %{buildroot}/%{_datadir}/%{name}/doc/html/.gitignore


%files
%license COPYING
%doc README.md
%{_qt5_archdatadir}/qml/Ubuntu/

%files doc
%doc %{_datadir}/%{name}/


%changelog
* Tue Feb 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.7-1 
- first try, inspiration from opensuse packaging

