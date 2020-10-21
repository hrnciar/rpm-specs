%global realver 0.1.1git1

Name:           srmio
Version:        0.1.1.1
Release:        3%{?dist}
Summary:        Schoberer Radmesstechnik (SRM) PowerControl access

License:        MIT
URL:            http://www.zuto.de/project/srmio/
Source0:        https://github.com/rclasen/%{name}/archive/v%{realver}.tar.gz#/%{name}-%{realver}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
App to access the most important functions of a Schoberer
Radmesstechnik (SRM) PowerControl V, VI and 7. You can download the data,
mark it deleted, sync the time and set the recording interval.

%package libs
Summary:        Library for %{name}

%description libs
This package contains library for %{name}.

%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development documentation
for %{name}.

%prep
%autosetup -n %{name}-%{realver}


%build
autoreconf -vfi
%configure \
    --enable-static=no
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la

%files
%{_bindir}/srmcmd
%{_bindir}/srmdump
%{_bindir}/srmsync
%{_mandir}/man1/srm*.1*

%files libs
%license LICENSE
%doc Changes README
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Vasiliy Glazov <vascom2@gmail.com> - 0.1.1.1.1-1
- Initial release
