%global somajor 0

Name:           libeconf
Version:        0.3.5
Release:        1%{?dist}
Summary:        Enhanced config file parser library

License:        MIT
URL:            https://github.com/openSUSE/libeconf
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make

%description
libeconf is a highly flexible and configurable library to parse and manage
key=value configuration files. It reads configuration file snippets from
different directories and builds the final configuration file from it.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
autoreconf -fiv
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -print -delete


%check
%make_build check


%files
%license LICENSE
%doc NEWS README.md TODO.md
%{_libdir}/%{name}.so.%{somajor}{,.*}

%files devel
%doc example/
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Feb 06 2020 Neal Gompa <ngompa13@gmail.com> - 0.3.5-1
- Update to 0.3.5 (RH#1797753)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Neal Gompa <ngompa13@gmail.com> - 0.3.4-1
- Update to 0.3.4 (RH#1793599)

* Wed Oct 30 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.3-1
- Update to 0.3.3 (RH#1756080)

* Tue Sep 24 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.1-1
- Update to 0.3.1 (RH#1755161)

* Fri Sep  6 2019 Neal Gompa <ngompa13@gmail.com> - 0.3.0-1
- Initial packaging for Fedora (RH#1749869)
