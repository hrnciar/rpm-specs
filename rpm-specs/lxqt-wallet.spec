%global srcname lxqt_wallet

Name:           %(echo %{srcname} |tr _ - )
Version:        3.1.0
Release:        9%{?dist}
Summary:        Create a kwallet like functionality for LXQt

License:        BSD
URL:            https://github.com/mhogomchungu/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(lxqt)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  libgcrypt-devel
BuildRequires:  qt5-linguist

%description
This project seeks to give a functionality for secure storage
of information that can be presented in key-values pair like
user names-passwords pairs.

Currently the project can store the information in KDE's kwallet,
GNOME's secret service or in an internal system that use libgcrypt
as its cryptographic backend.

The internal secure storage system allows the functionality to
be provided without dependencies on KDE or GNOME libraries.

This project is designed to be used by other projects simply by
adding the source folder in the build system and start using it.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblxqt-devel%{?_isa}

%description devel
%{summary}.


%prep
%autosetup -n%{srcname}-%{version}
cp -p backend/README README-backend
cp -p frontend/README README-frontend

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake_lxqt \
 -DQT5=true \
 -DLIB_SUFFIX=default \
 -DNOKDESUPPORT=false \
 -DNOSECRETSUPPORT=false \
 -DBUILD_SHARED=true \
 ..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang %{name} --with-qt


%ldconfig_scriptlets


%files -f %{name}.lang
%license LICENSE
%doc README.md changelog
%{_bindir}/%{srcname}-cli
%{_libdir}/*.so.*

%files devel
%doc README-*
%{_includedir}/lxqt/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Christian Dersch <lupinix@mailbox.org> - 3.1.0-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-2
- rebuilt for latest Qt5

* Wed Aug 03 2016 Raphael Groner <projects.rg@smart.ms> - 3.0.0-1
- new version
- drop hacks for translations and pkgconfig
- readd gcc-c++

* Sat Jul 23 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.1-2
- fix compilation of translations
- add hack for pkgconfig version

* Thu Jul 14 2016 Raphael Groner <projects.rg@smart.ms> - 2.2.1-1
- initial
